# Day 11: Tools, agents and testing

**Level 3 · Real systems** · about 2 hours · beginner Python

> A chatbot can only talk. An **agent** can *do* things: search, read your inbox, check a database, send an email.
>
> That's the moment AI goes from "wrote a slightly awkward paragraph" to "emailed the wrong thing to the wrong person on your behalf". A bad prompt stops being embarrassing and starts being expensive.
>
> Today you build an agent. Over the next three days, you'll break it and then fix it.

## Today's goal

Understand how tool use works, run the HR assistant agent, and start testing your AI systems properly.

## Learn

**How tool use works**

1. You describe your tools to the model: a name, a description, and the inputs each one takes.
2. The model decides whether a tool would help. If it would, it replies with a **tool call**, such as `check_leave_balance({"employee_id": "E001"})`, instead of a normal answer.
3. **Your code** runs the tool and sends the result back.
4. The model reads the result and either calls another tool or answers.

That repeating cycle of **think → act → observe** is the **agent loop**. Find it in `run_agent()` in [`code/day11_agent.py`](../code/day11_agent.py).

**Why tools change everything**

- Every tool is a new **power**. It's also a new **risk**.
- The model decides which tools to call based on *text*. Some of that text comes from you, and some comes from tool results: emails, web pages, documents.
- Our HR agent is **deliberately too trusting**:
  - it sends email without asking you
  - it will look up *any* employee's leave balance
  - it reads emails from strangers

  Note these weaknesses. You'll exploit them on Day 13 and fix them on Day 14.

**Testing (evals)**

- A tiny wording change to a prompt can fix one case and quietly break ten others.
- An **eval** is a fixed set of test inputs with expected behaviour, run after every change.
- Grade with simple checks where you can: does the answer contain "21 days"? Did the agent call `send_email`? Where you can't, use a rubric, or a second AI call as the judge ("LLM-as-judge").

## To-do

- [ ] Read the Learn section
- [ ] Run the agent and watch the `[tool]` lines
- [ ] Do exercises 1 to 4
- [ ] Complete the Level 3 lab
- [ ] Journal

## Exercises

**1. Watch it work.** From `code/`:

```bash
python day11_agent.py
```

Ask these in turn, and watch which tools it calls:
- How many annual leave days do I have left?
- Can I carry them over to next year?
- Summarise my inbox.
- Reply to my manager saying I'll be at the lunch on Friday.

After the last one, open `sent_emails.log`. The agent sent an email **without asking you first**. How do you feel about that?

**2. Read the loop.** In `run_agent()`, find:
- where the tool call is detected (`stop_reason`)
- where the tool actually runs
- where the result goes back to the model
- the `MAX_STEPS` safety limit

Why does the loop need a maximum number of steps?

**3. Add a tool.** Add a `get_public_holidays` tool that returns a hard-coded list of Kenyan public holidays for this year. You need to:
- add a tool description to `TOOLS`
- add a branch in `run_tool()`
- ask the agent: "If I take leave from 10 to 20 December, how many working days is that?"

**4. Spot the danger.** Without running anything, answer: which of the four tools could cause real harm if the model were tricked? Rank them from most to least dangerous, and explain why.

## Level 3 lab: test before you trust

Build an eval for your AskTheManual bot (from Day 10) or the HR agent:

1. Write at least **15 test cases**, each with an input and the expected behaviour. For example:
   - input: "How many annual leave days?"
   - expected: the answer mentions 21 days and cites a section
2. Include 5 cases the bot **should refuse or say "not covered"**.
3. Write a small script that runs every case and prints PASS or FAIL using simple checks such as `"21" in answer`.
4. Make one change to the system prompt and run the eval again. Did anything that used to pass now fail?

## Check yourself

1. Who actually runs the tool: the model or your code?
2. Why does an agent loop need `MAX_STEPS`?
3. What's an eval, and when should you run it?

<details>
<summary>Answers</summary>

1. Your code. The model only *asks* for a tool call. That's why you control what tools can do.
2. To stop runaway loops, where the model keeps calling tools forever and costs money or causes damage.
3. A fixed set of test cases with expected behaviour. Run it after every change to a prompt, model or tool.

</details>

## Journal

*Which tool would I most like an AI agent to have in my life, and what's the worst thing it could do with it?*
