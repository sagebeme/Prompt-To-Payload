"""Day 9: your first prompt through an API.

Run:  python day09_first_call.py
Needs the ANTHROPIC_API_KEY environment variable (see days/day-09.md).
"""

import anthropic

MODEL = "claude-opus-5"

# Reads ANTHROPIC_API_KEY from the environment. Never paste your key into code.
client = anthropic.Anthropic()


def ask(system: str, question: str, effort: str = "medium") -> str:
    """Send one question with a system prompt and return the text reply."""
    response = client.messages.create(
        model=MODEL,
        max_tokens=4000,
        system=system,
        messages=[{"role": "user", "content": question}],
        # effort: "low" is faster and cheaper, "high" thinks harder.
        output_config={"effort": effort},
        # If a safety check declines the request, let the API retry it on a
        # suitable fallback model instead of just stopping.
        extra_headers={"anthropic-beta": "server-side-fallback-2026-07-01"},
        extra_body={"fallbacks": "default"},
    )

    if response.stop_reason == "refusal":
        return "[The model declined this request.]"

    # The reply is a list of blocks. We only want the text ones.
    return "".join(block.text for block in response.content if block.type == "text")


if __name__ == "__main__":
    system = (
        "You are a friendly tutor who explains tech to people in Kenya "
        "using everyday local examples. Keep answers under 80 words."
    )
    print(ask(system, "What is an API?"))

    # Exercise 2: run the same prompt over a list of inputs.
    for thing in ["a database", "the cloud", "encryption"]:
        print(f"\n--- {thing} ---")
        print(ask(system, f"What is {thing}?", effort="low"))
