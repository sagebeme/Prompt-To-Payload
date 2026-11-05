# Setup and troubleshooting

Days 1–8 need only an AI chat app. Days 9–14 run the Python scripts in [`code/`](code/). This page gets you set up for those, and helps when something goes wrong. [Day 9](days/day-09.md) walks through the same steps as a lesson.

## What you need

- **Python 3.10 or newer.** Check with `python3 --version` (Windows: `python --version`). The `anthropic` SDK will not install on older versions.
- **A terminal** and a text editor.
- **An Anthropic API key** with a small amount of credit.

## Install

From the repo's `code/` folder:

```bash
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

Activate the virtual environment again (`source .venv/bin/activate`) every time you open a new terminal.

## Get an API key safely

1. Sign in at [platform.claude.com](https://platform.claude.com) and add a small amount of credit. Setting a monthly spend limit there is a good idea.
2. Create a key and copy it once. Treat it like a password.
3. Put it in an environment variable, not in code:

   ```bash
   export ANTHROPIC_API_KEY="your-key-here"   # Windows PowerShell: $env:ANTHROPIC_API_KEY="your-key-here"
   ```

   Or copy `code/.env.example` to `code/.env`, fill it in, and load it with `set -a; source .env; set +a`. `.env` is ignored by Git.
4. Never paste a key into code, screenshots, chat messages or a Git repository. If one leaks, revoke it in the console straight away and make a new one.

Check it works:

```bash
python day09_first_call.py
```

[`code/README.md`](code/README.md) lists how to run every script.

## Troubleshooting

**`TypeError: "Could not resolve authentication method..."`**
The key isn't set in this terminal. Run the `export` line again (or `source .env`) in the same terminal you run Python from, then check with `echo $ANTHROPIC_API_KEY` (PowerShell: `echo $env:ANTHROPIC_API_KEY`). A new terminal starts without it.

**`anthropic.AuthenticationError` (401, "invalid x-api-key")**
The key is set but wrong: mistyped, cut off when copying, has extra quotes or spaces, or was revoked. Create a new key in the console and set it again.

**A 400 error that mentions your credit balance**
The account has no credit left. Add some in the console's billing page.

**`anthropic.RateLimitError` (429)**
You're sending requests faster than your account allows. The SDK already retries a couple of times; if it still fails, wait a minute and try again, and slow down loops (for example on Day 9 exercise 3) with a short `time.sleep(1)` between calls. New accounts have lower limits that rise with use.

**`anthropic.InternalServerError` or "overloaded" (500, 529)**
A temporary problem on the API side. Wait a little and run it again.

**`ModuleNotFoundError: No module named 'anthropic'`**
The virtual environment isn't active, or the install didn't run. Activate it and run `pip install -r requirements.txt` again.

**`ERROR: No matching distribution found for anthropic==...` or `Requires-Python >=3.10`**
Your Python is too old. Install Python 3.10 or newer, delete the `.venv` folder, and create it again with the new Python.

**Windows: "running scripts is disabled on this system" when activating**
PowerShell blocks the activate script by default. Use Command Prompt (`.venv\Scripts\activate.bat`) instead, or allow scripts for your user only: `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`.

**The course website says "This lesson couldn't load"**
You opened the HTML file straight from disk. Serve the folder instead: `python3 -m http.server 8000` in the repo, then open http://localhost:8000.
