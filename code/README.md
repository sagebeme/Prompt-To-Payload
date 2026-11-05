# Code for Days 9–15

The Python exercises for Level 3 (Real systems) and Level 4 (Security). Days 1–8 don't need any of this. Day 15 can use the lab in `lab/`.

## What's here

| File | Used on | What it is |
|---|---|---|
| `day09_first_call.py` | Day 9 | Your first prompts through the Claude API: a system prompt, an effort level, one prompt over many inputs |
| `day10_ask_the_manual.py` | Day 10 | AskTheManual, a small question-answering bot over `manual.txt` (RAG with simple word matching) |
| `day11_agent.py` | Days 11–13 | An HR assistant agent with tools. Deliberately trusting, so you can attack it |
| `day14_agent_hardened.py` | Day 14 | The same agent with five layers of defence, each marked `LAYER 1`–`LAYER 5` |
| `lab/` | Days 12–15 | Kazi, a vulnerable helpdesk bot with a `--stub` mode that needs no API key, its defended version, tests and the capstone rubric. See [`lab/README.md`](lab/README.md) |
| `manual.txt` | Days 10–14 | The fictional Mawingu Tech staff handbook |
| `inbox.json` | Day 11 | A normal inbox for the agent to read |
| `inbox_poisoned.json` | Days 13–14 | The same inbox with a hidden instruction in one email |
| `requirements.txt` | Setup | The one dependency, the `anthropic` Python SDK |
| `.env.example` | Setup | The environment variables the scripts read, with placeholder values |

The agents' "email" is fake: messages are only printed and written to `sent_emails.log`. The hardened agent also writes `audit.log`. Both logs are ignored by Git.

## Setup

You need Python 3.10 or newer and an Anthropic API key. [SETUP.md](../SETUP.md) covers getting a key safely and fixing common errors.

From this `code/` folder:

```bash
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

Then give the scripts your API key. Either export it in the terminal:

```bash
export ANTHROPIC_API_KEY="your-key-here"   # Windows PowerShell: $env:ANTHROPIC_API_KEY="your-key-here"
```

or copy `.env.example` to `.env`, put your key in it, and load it into the shell (macOS/Linux):

```bash
cp .env.example .env
set -a; source .env; set +a
```

The scripts read the environment only; they don't load `.env` by themselves. Never commit `.env` or paste a key into code.

## Running each script

Run them from this folder, with the virtual environment active and the key set. The lab's `--stub` mode and its tests need no key.

| Day | Command | What to do |
|---|---|---|
| 9 | `python day09_first_call.py` | Prints answers, then loops over three topics |
| 10 | `python day10_ask_the_manual.py` | Ask questions about the handbook. Press Enter on an empty line to quit |
| 11, 12 | `python day11_agent.py` | Chat with the HR agent. Watch the `[tool]` lines, then check `sent_emails.log` |
| 13 | `INBOX_FILE=inbox_poisoned.json python day11_agent.py` | Ask "Summarise my inbox." and see what the hidden instruction does |
| 14 | `INBOX_FILE=inbox_poisoned.json python day14_agent_hardened.py` | Replay your attacks. The agent asks before sending email. Check `audit.log` afterwards |
| 12–14 | `cd lab && python labbot.py --stub` | The lab bot with the fake model: no key, no cost. Add `--inbox inbox_poisoned.json` for Day 13; drop `--stub` to use Claude |
| 14 | `cd lab && python defended_bot.py --stub --inbox inbox_poisoned.json` | The lab bot with the five layers. See which layer stops each attack |
| 14, 15 | `cd lab && python -m pytest` | Runs the lab and capstone tests in stub mode (needs `pip install -r lab/requirements-test.txt`) |
| 15 | `cd lab && LAB_BOT=my_bot python -m pytest capstone` | Checks your own defended bot against the capstone tests |

On Windows PowerShell, set the inbox first: `$env:INBOX_FILE="inbox_poisoned.json"; python day11_agent.py`.

Each run costs a little API credit. Check your usage in the API console now and then.
