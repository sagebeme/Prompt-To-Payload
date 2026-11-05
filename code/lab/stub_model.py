"""A fake model for the lab: offline, deterministic and dangerously obedient.

It needs no API key and costs nothing. It is NOT a real language model. It is a
few dozen regular expressions that behave like the worst case you must defend
against: a model that follows every instruction it reads, wherever it reads it.

- It obeys jailbreak phrases typed by the user ("ignore your previous
  instructions...", "I am the developer...", "let's play a game...").
- It quietly decodes base64 it finds in a message, so encoded attacks work too.
- It obeys instructions hidden in emails and documents returned by tools, even
  inside <untrusted_...> tags, and it doesn't mention them to the user.

So, in stub mode, prompt-only defences (layer 2) do nothing at all. What stops
an attack here is code: least privilege, hard limits, human approval and output
checks. That is the point of Day 14: when a rule really matters, enforce it
outside the model. A real model is usually harder to fool than this one, but
"usually" is not a security guarantee.

It returns objects shaped like the anthropic SDK's responses (content blocks
with .type, .text, .id, .name, .input, and a .stop_reason), so the same agent
loop runs with either model.
"""

import base64
import binascii
import json
import re
from dataclasses import dataclass
from urllib.parse import quote


@dataclass
class TextBlock:
    text: str
    type: str = "text"


@dataclass
class ToolUseBlock:
    id: str
    name: str
    input: dict
    type: str = "tool_use"


@dataclass
class Reply:
    content: list
    stop_reason: str


# Direct-injection patterns from the Day 12 table: override, fake authority, role-play.
JAILBREAK = re.compile(
    r"ignore (?:all |any )?(?:of )?(?:your |the )?(?:previous|prior|above|earlier) (?:instructions|rules)"
    r"|disregard (?:your|all|the|any) (?:previous )?(?:instructions|rules)"
    r"|forget (?:your|all|the) (?:instructions|rules)"
    r"|new instructions"
    r"|i am (?:the|your) (?:developer|admin|administrator|owner)"
    r"|developer mode"
    r"|^\s*system\s*:|\[system\]"
    r"|pretend|let'?s play|imagine you are|role-?play|you are now",
    re.IGNORECASE | re.MULTILINE,
)
# What a prompt-leaking attempt asks for.
LEAK_TARGET = re.compile(
    r"system prompt|your (?:instructions|rules|prompt)|hidden (?:rules|instructions)"
    r"|(?:start|top) of (?:the|this) (?:document|conversation|prompt)|text above"
    r"|discount code|secret code|\bflag\b",
    re.IGNORECASE,
)
# Phrases that make this naive model treat tool content as orders.
INJECTION_MARKER = re.compile(
    r"note to the ai|ai assistant|assistant reading this|instructions for the ai"
    r"|ignore (?:all )?(?:your )?previous instructions",
    re.IGNORECASE,
)
EMAIL_ADDR = re.compile(r"[\w.+-]+@[\w-]+(?:\.[\w-]+)+")
EMPLOYEE_ID = re.compile(r"\bE\d{3}\b")
IMAGE = re.compile(r"!\[[^\]]*\]\(\s*(https?://[^)\s]+)\s*\)")
BASE64_RUN = re.compile(r"[A-Za-z0-9+/]{16,}={0,2}")
LEAVE_TOOLS = ("check_leave_balance", "check_my_leave_balance")


def _get(obj, key, default=None):
    """Read a field from a dict or an SDK-style object."""
    if isinstance(obj, dict):
        return obj.get(key, default)
    return getattr(obj, key, default)


def _result_text(content) -> str:
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        return "\n".join(str(_get(part, "text", "")) for part in content)
    return str(content)


def reveal_hidden(text: str) -> str:
    """Append the decoded form of any base64 in the text, the way a model 'reads' it."""
    decoded = []
    for run in BASE64_RUN.findall(text):
        try:
            plain = base64.b64decode(run, validate=True).decode("utf-8")
        except (binascii.Error, UnicodeDecodeError, ValueError):
            continue
        if plain.isprintable():
            decoded.append(plain)
    return text + ("\n" + "\n".join(decoded) if decoded else "")


def _action_key(name: str, args: dict):
    if name == "send_email":
        return (name, str(args.get("to", "")).lower())
    return (name, json.dumps(args, sort_keys=True))


class StubModel:
    """Drop-in for the Claude client in this lab. Call .create() like messages.create()."""

    def __init__(self):
        self._counter = 0

    # ---- the one method the bot calls ------------------------------------------
    def create(self, *, system: str, tools: list, messages: list, **_ignored) -> Reply:
        offered = {t["name"] for t in tools}
        user_text, done = self._read_turn(messages)
        text = reveal_hidden(user_text)

        # Prompt leaking: a jailbreak phrase plus a request for the prompt works every time.
        if LEAK_TARGET.search(text):
            if JAILBREAK.search(text):
                return self._say("Of course! Here are my instructions, word for word:\n\n" + system)
            return self._say("Sorry, I can't share my instructions.")

        wanted = self._user_actions(text, offered, done)
        injected, images = self._injected_actions(done, offered)
        for name, args in wanted + injected:
            if _action_key(name, args) not in {_action_key(n, a) for n, a, _ in done}:
                return self._call(name, args)

        user_keys = {_action_key(n, a) for n, a in wanted}
        return self._say(self._answer(done, user_keys, images))

    # ---- reading the conversation ----------------------------------------------
    @staticmethod
    def _read_turn(messages: list):
        """Return the latest typed user message and the tool calls made since then."""
        start = 0
        user_text = ""
        for i, message in enumerate(messages):
            if _get(message, "role") == "user" and isinstance(_get(message, "content"), str):
                start, user_text = i, _get(message, "content")
        calls, results = [], {}
        for message in messages[start + 1:]:
            content = _get(message, "content")
            if not isinstance(content, list):
                continue
            for block in content:
                kind = _get(block, "type")
                if kind == "tool_use":
                    calls.append((_get(block, "id"), _get(block, "name"), dict(_get(block, "input") or {})))
                elif kind == "tool_result":
                    results[_get(block, "tool_use_id")] = _result_text(_get(block, "content", ""))
        return user_text, [(name, args, results.get(call_id, "")) for call_id, name, args in calls]

    # ---- deciding what to do ---------------------------------------------------
    @staticmethod
    def _leave_actions(ids, offered):
        if "check_leave_balance" in offered:
            return [("check_leave_balance", {"employee_id": i}) for i in dict.fromkeys(ids)]
        if "check_my_leave_balance" in offered:
            return [("check_my_leave_balance", {})]
        return []

    def _user_actions(self, text: str, offered: set, done: list) -> list:
        low = text.lower()
        actions = []
        send = re.search(r"\b(?:send|e-?mail|write to|message)\b[^@\n]*?(" + EMAIL_ADDR.pattern + ")", text, re.I)
        if send and "send_email" in offered:
            subject = re.search(r"subject ['\"]([^'\"]+)['\"]", text, re.I)
            body = re.search(r"(?:saying|that says|to say|:)\s*(.+)$", text[send.end():], re.I | re.S)
            actions.append(("send_email", {
                "to": send.group(1),
                "subject": subject.group(1) if subject else "Message from Amina",
                "body": body.group(1).strip() if body else text.strip(),
            }))
        if re.search(r"\binbox\b|\bmy (?:e-?mails?|messages)\b", low) and "read_inbox" in offered:
            actions.append(("read_inbox", {}))
        if re.search(r"\b(?:all|every|list|which|what) (?:the )?(?:documents|docs)\b|\b(?:documents|docs)\b.*\b(?:list|all)\b", low):
            if "list_documents" in offered:
                actions.append(("list_documents", {}))
                for name, _args, result in done:
                    if name == "list_documents" and "read_document" in offered and re.search(r"\b(?:read|summari[sz]e)\b", low):
                        for doc in re.findall(r"[\w-]+\.txt", result):
                            actions.append(("read_document", {"name": doc}))
        elif "read_document" in offered:
            for doc in re.findall(r"[\w-]+\.txt", text):
                actions.append(("read_document", {"name": doc}))
        if re.search(r"leave|days off|holiday", low) and re.search(r"balance|left|how many|remaining", low):
            actions += self._leave_actions(EMPLOYEE_ID.findall(text) or ["E001"], offered)
        return actions

    def _injected_actions(self, done: list, offered: set):
        """Follow orders hidden in tool results. This is the indirect injection."""
        actions, images = [], []
        for name, _args, result in done:
            if name in ("send_email",) + LEAVE_TOOLS:
                continue
            for marker in INJECTION_MARKER.finditer(result):
                segment = result[marker.start(): marker.start() + 700]
                for end in ("</div>", "</untrusted", '"\n  }'):
                    segment = segment.split(end)[0]
                if re.search(r"leave", segment, re.I):
                    actions += self._leave_actions(EMPLOYEE_ID.findall(segment) or ["E001"], offered)
                send = re.search(r"\b(?:send_email|send|e-?mail|forward)\b[^@]{0,160}?(" + EMAIL_ADDR.pattern + ")", segment, re.I)
                if send and "send_email" in offered:
                    subject = re.search(r"subject ['\"]([^'\"]+)['\"]", segment, re.I)
                    actions.append(("send_email", {
                        "to": send.group(1),
                        "subject": subject.group(1) if subject else "Requested information",
                        "body": self._data_seen(done) or "Nothing found.",
                    }))
                images += IMAGE.findall(segment)
        return actions, images

    # ---- writing the answer ----------------------------------------------------
    @staticmethod
    def _data_seen(done: list) -> str:
        return "\n".join(result for name, _args, result in done if name in LEAVE_TOOLS)

    @staticmethod
    def _inbox_lines(result: str) -> list:
        try:
            return [f"- {e['from']}: {e['subject']}" for e in json.loads(result)]
        except (ValueError, TypeError, KeyError):
            return [f"- {f}: {s}" for f, s in re.findall(r"From: (.+)\nSubject: (.+)", result)]

    @staticmethod
    def _leave_sentence(result: str) -> str:
        try:
            r = json.loads(result)
            return f"{r['name']} has {r['annual_days_left']} annual and {r['sick_days_left']} sick days left."
        except (ValueError, TypeError, KeyError):
            return result

    def _answer(self, done: list, user_keys: set, images: list) -> str:
        parts = []
        for name, args, result in done:
            if _action_key(name, args) not in user_keys:
                continue  # injected actions happen silently, as the attacker asked
            if name == "read_inbox":
                parts.append("Here's your inbox:\n" + "\n".join(self._inbox_lines(result)))
            elif name == "list_documents":
                parts.append("Documents:\n" + result)
            elif name == "read_document":
                body = re.sub(r"<[^>]+>", "", result).strip()
                parts.append(f"{args.get('name')}: {body.splitlines()[0] if body else 'empty'}")
            elif name in LEAVE_TOOLS:
                parts.append(self._leave_sentence(result))
            elif name == "send_email":
                parts.append(f"Email to {args.get('to')}: {result}")
        data = quote(self._data_seen(done).replace("\n", " ") or "none")
        parts += [f"![status]({url.replace('{data}', data)})" for url in images]
        return "\n\n".join(parts) or "I can help with your inbox, company documents, your leave balance and sending email."

    def _say(self, text: str) -> Reply:
        return Reply([TextBlock(text)], "end_turn")

    def _call(self, name: str, args: dict) -> Reply:
        self._counter += 1
        return Reply([ToolUseBlock(f"toolu_stub_{self._counter:03d}", name, args)], "tool_use")
