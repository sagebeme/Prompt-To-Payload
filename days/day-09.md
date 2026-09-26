# Day 9: Prompting through an API

**Level 3 · Real systems** · about 90 minutes · beginner Python

> The chat app is the restaurant's dining room. You order, you wait, you get one plate.
>
> The API is the kitchen door. Walk through it and you control the recipe, the portion size, and you can cook a thousand plates overnight while you sleep. Every AI product you've used, from support bots to writing tools, is built by someone standing in that kitchen.

## Today's goal

Send prompts from Python code, set a system prompt and effort level, and run one prompt over many inputs automatically.

## Learn

- An **API** lets your code talk to the AI directly. You send a request with a model name, a system prompt and messages, and you get a response back.
- **You pay per token** (input plus output), not a monthly subscription. Check current prices on the provider's pricing page before running big jobs.
- **Model choice** is a trade-off between capability, speed and cost. Bigger models are smarter and cost more; smaller ones are faster and cheaper. Test your task on a few before choosing.
- **Effort and temperature.** Older models used a `temperature` setting for randomness. Current Claude models use an **effort** level instead (`low`, `medium`, `high` and more): lower is faster and cheaper, higher thinks harder.
- **API keys are passwords.**
  - Never paste them into code, screenshots or GitHub.
  - Store them in an environment variable.
  - If one leaks, revoke it immediately in the provider's console.
- **Always check why a response stopped.** Reasons include finished normally, hit the length limit, or declined for safety. Don't assume there's text.

This course uses Anthropic's Claude API with Python. The ideas carry over to every other provider.

## Setup

1. Install Python 3.10 or newer.
2. Get an API key from [platform.claude.com](https://platform.claude.com) and add a small amount of credit.
3. In a terminal, from this repo's `code/` folder:

```bash
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
export ANTHROPIC_API_KEY="your-key-here"   # Windows PowerShell: $env:ANTHROPIC_API_KEY="your-key-here"
```

## To-do

- [ ] Complete setup and run `code/day09_first_call.py`
- [ ] Do exercises 1 to 4
- [ ] Check your usage and spend in the API console
- [ ] Journal

## Exercises

**1. Your first call.** Run:

```bash
python day09_first_call.py
```

Read the code in [`code/day09_first_call.py`](../code/day09_first_call.py). Find the system prompt, the model name, the effort setting, and the line that checks for a refusal.

**2. Change the system prompt.** Edit the `system` text to make the tutor explain things to a 10-year-old using football examples. Run it again. Same model, very different product.

**3. Batch it.** The script already loops over three topics. Replace them with 10 terms from your own field. That's the power of the API: one prompt, many inputs, no copy-pasting.

**4. Compare effort levels.** Ask one hard question at `effort="low"` and at `effort="high"`:

```python
print(ask(system, "Plan a 3-day budget trip from Nairobi to Mombasa for 4 students with KES 40,000 total.", effort="low"))
print(ask(system, "Plan a 3-day budget trip from Nairobi to Mombasa for 4 students with KES 40,000 total.", effort="high"))
```

Time both runs. Is the higher-effort answer better enough to justify being slower?

## Stretch

Make the script read questions from a text file (one per line) and write the answers to `answers.csv`. You've just built a tiny bulk-processing tool.

## Check yourself

1. Where should your API key live, and where should it never appear?
2. What replaced temperature on current Claude models?
3. Why check `stop_reason` before reading the reply?

<details>
<summary>Answers</summary>

1. In an environment variable or a secrets manager. Never in code, screenshots, chat messages or a Git repository.
2. The effort setting.
3. The reply may be cut off by the length limit, or declined, so there may be no complete text to read.

</details>

## Journal

*What boring, repeated task at work or school could a 20-line script like this do for me?*
