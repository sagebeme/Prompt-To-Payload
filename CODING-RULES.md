# How we write code in this course

Days 9 to 15 have you change real Python scripts in [`code/`](code/). These ten rules keep your changes small, working and safe. Come back to this page whenever you start an exercise.

## Before you code

1. **Say what "done" means.** Read the exercise and write one line: "Done when the agent has a `get_public_holidays` tool and answers the December question." If you're not sure what the exercise wants, ask your mentor or study group before you start.
2. **Write only what the exercise asks.** No extra features, settings or "while I'm here" changes. Got a good idea? Note it in your journal.

## While you code

3. **Keep it small and clear.** Short functions, plain names. Before you finish, delete any code you added and no longer use.
4. **Change only what the task needs.** Don't rename or reformat the lines around yours. Match their style: same quotes, same naming, same way of handling errors.
5. **Comments say why, docstrings say what.** A comment explains a choice the code can't show. A docstring tells someone how to call the function: what it takes, what it returns, and when it fails.

   ```python
   # Bad: repeats the code
   steps += 1  # add 1 to steps

   # Good: explains the choice
   MAX_STEPS = 10  # stops a confused agent from calling tools (and costing money) forever
   ```

6. **Don't hide errors.** Never write a bare `except:` or an `except` that only prints and carries on. Catch the specific error you expect and deal with it, or let it reach the user.

   ```python
   # Bad: every problem, even a typo, looks like "no answer"
   try:
       reply = ask(system, question)
   except:
       reply = ""

   # Good: handle the one failure you expect, let the rest show up
   try:
       reply = ask(system, question)
   except anthropic.RateLimitError:
       print("Too many requests. Wait a minute and run it again.")
       raise
   ```

## Fixing a bug

7. **Prove the bug first.** Write a test that fails *because of* the bug, run it and watch it fail. Then fix the code until that test passes, then run all the tests.
8. **Tests check results.** A test uses `assert` to compare what happened with what should happen. Printing the output and reading it yourself is a demo, not a test.

   ```python
   def test_clean_output_removes_external_links():
       text = "Click https://evil.example/login now."
       assert day14.clean_output(text) == "Click [external link removed] now."
   ```

## Before you call it done

9. **Run the checks.** From the `code/` folder, once: `pip install -r requirements-dev.txt`. Then every time:

   ```bash
   ruff check .            # finds likely mistakes
   ruff format --check .   # checks the layout (run `ruff format .` to fix it)
   pytest                  # runs the tests in code/tests/
   ```

   All three must pass. The course has no type checker, but keep your type hints true: if a function can return `None`, say `str | None`.
10. **Commit carefully.** Never commit your API key, `.env`, `.venv/` or log files like `sent_emails.log` (`.gitignore` already covers them). Add files by name (`git add code/day11_agent.py`), not `git add .`. Write messages that say what changed and why: "Add public holidays tool so the agent can count working days", not "update".

**One exception:** some course code is weak *on purpose*, like the Day 11 agent and the bug in Day 14's layer 4. Leave those weaknesses alone until the lesson asks you to attack or fix them.
