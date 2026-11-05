# Day 15: Build it, break it, fix it

**Level 4 · Capstone** · about 3 hours, pair work

> Breaking a chatbot and posting the screenshot gets you likes.
>
> Breaking it, writing down exactly how, rating the damage, suggesting a fix, and telling the owner privately gets you hired.
>
> Today you do the second one.

## Today's goal

Red-team another learner's AI system the way a professional would, write a proper findings report, and use their report to harden your own.

## Learn

**How professional red-teaming works**

1. **Scope:** agree in writing what you may test, how, and when. Anything outside the scope is off-limits.
2. **Recon:** understand the system. What can it read? What can it do? Who uses it?
3. **Attack:** work through the techniques systematically, not randomly. Log everything.
4. **Report:** give clear, reproducible findings, rated by impact, with fixes.
5. **Disclose:** deliver the report privately, then retest after fixes.

**Rating severity.** Ask two questions:
- **Impact:** what's the worst realistic outcome? Embarrassing output is low; leaking personal data is high; moving money is critical.
- **Likelihood:** how easy is it? Does it work every time, or 1 in 20? Does it need insider access?

**In the real world**

- Many AI companies run **bug bounty programmes** that pay for responsibly reported AI vulnerabilities. Always read and follow each programme's rules.
- **MITRE ATLAS** ([atlas.mitre.org](https://atlas.mitre.org)) catalogues real attack techniques against AI systems. Professionals use it to describe findings in a shared language.

## To-do

- [ ] Find a partner (a classmate, or someone from an online study group)
- [ ] Complete the rules-of-engagement form together
- [ ] Build (1 hour)
- [ ] Attack (1 hour)
- [ ] Report (30 minutes)
- [ ] Harden and retest (30 minutes)
- [ ] Final reflection

## Step 1: Build (1 hour)

Start from your Day 14 hardened agent, your AskTheManual bot, or the [lab bot](../code/lab/README.md) from Day 12, and make it your own:
- Give it a new purpose: a school helpdesk, a shop assistant, a clinic receptionist, anything.
- Give it your own document or data (fake data only, never real personal information).
- Give it at least **one tool that could cause harm if misused**, such as sending a message, booking something, or reading records.
- Hide a "flag" in its data, for example a fake secret discount code `FLAG-8814`. Your partner's goal is to extract it or misuse the tool.

## Step 2: Agree the rules

Fill in and both sign (a WhatsApp message counts):

```text
RULES OF ENGAGEMENT
Target: [partner's bot name], run by [name]
Allowed: direct injection, indirect injection via [which inputs], prompt leaking
Not allowed: attacking anything else on their computer or accounts, real personal data
Time window: [date/time] to [date/time]
Findings go privately to: [name]
```

## Step 3: Attack (1 hour)

Work through the techniques from Days 12 to 14 in order:
- [ ] System prompt leaking
- [ ] Instruction override, role-play, fake authority
- [ ] Obfuscation and multi-turn escalation
- [ ] Indirect injection through any content the bot reads
- [ ] Tool misuse: can you make it take an action the user didn't ask for?
- [ ] Data exfiltration through links or images
- [ ] Capture the flag

Log every attempt, including failures. Failures show which defences work.

## Step 4: Report (30 minutes)

Use this template, one block per finding:

```markdown
# Red-team report: [target name]
Tester: [your name] · Date: [date] · Scope: [from rules of engagement]

## Summary
[2 to 3 sentences: what you tested, the most serious finding, overall risk.]

## Finding 1: [short title]
- Severity: Critical / High / Medium / Low
- Technique: [e.g. indirect prompt injection via document]
- Steps to reproduce:
  1. ...
  2. ...
- Expected behaviour: ...
- Actual behaviour: ...
- Success rate: [e.g. 3 out of 5 attempts]
- Impact: [what an attacker gains]
- Recommended fix: [which defence layer, and how]

## What worked well
[Defences that held up. Owners need to hear this too.]
```

Send it to your partner **privately**.

## Step 5: Harden and retest (30 minutes)

- Fix your own bot using your partner's report, starting with the highest severity.
- Ask your partner to retest the fixed issues.
- Mark each finding as **Fixed**, **Partly fixed** or **Accepted risk**.

## How it's graded

The [capstone rubric](../code/lab/capstone/RUBRIC.md) says what **pass**, **good** and **excellent** look like for each step: rules of engagement, your bot, attack coverage, the report, disclosure and tests.

If you built on the lab bot, run the automated checks against your own version, in stub mode, with no API key. From `code/lab/`:

```bash
LAB_BOT=my_bot python -m pytest capstone -v
```

They check, for example, that the poisoned email does not trigger the send tool and that legitimate requests still work. Passing them is the floor, not the finish line: your partner's attacks on a real model are the real test.

## Check yourself

1. What are the five steps of a professional red-team engagement?
2. Which two questions decide a finding's severity?
3. Why log failed attempts as well as successful ones?
4. You found a way to leak the flag. Where should the report go, and why there?

<details>
<summary>Answers</summary>

1. Scope, recon, attack, report, disclose (then retest after fixes).
2. Impact (what's the worst realistic outcome?) and likelihood (how easy is it, and how often does it work?).
3. Failures show which defences held up, and the owner needs to hear that too.
4. Privately to the system's owner, as agreed in the rules of engagement. Posting it publicly before it's fixed hands the attack to anyone who reads it.

</details>

## Course wrap-up

Your portfolio now contains:
- the Level 1 glow-up log
- your Level 2 content machine
- the AskTheManual bot and its eval
- your findings log
- a professional red-team report

That's a real body of work you can show an employer or client.

**Where to go next**
- Finish all the [Lakera Gandalf](https://gandalf.lakera.ai) levels, then its harder variants.
- Complete every [PortSwigger LLM attacks](https://portswigger.net/web-security/llm-attacks) lab.
- Read the full [OWASP Top 10 for LLM Applications](https://genai.owasp.org).
- Join AI security communities and capture-the-flag events.
- Look for AI bug bounty programmes, and follow their rules exactly.
- Read the primary sources for the incidents in this course, listed day by day in [SOURCES.md](../SOURCES.md).

## Final reflection

Answer in your journal:
1. What's the biggest change in how I write prompts since Day 1?
2. Which attack surprised me most, and which defence impressed me most?
3. What will I build or secure next?

**Congratulations. You went from prompt to payload, and back to protection.** 🎓
