# Day 5: Let it think

**Level 2 · Techniques** · about 60 minutes · no coding

> Ask a friend a tricky maths question and demand an answer in two seconds, and they'll probably blurt out something wrong. Hand them a napkin and a pen, and they'll get there.
>
> AI models are surprisingly similar. When they write out their reasoning before answering, they make fewer mistakes on maths, logic and planning. Many newer models now do this "thinking" automatically in the background. Knowing how to ask for it, and how to structure it, still makes a big difference.

## Today's goal

Get better answers on hard problems by asking for step-by-step reasoning, breaking problems down, and making the model check itself.

## Learn

- **Step-by-step reasoning** (often called "chain of thought"): ask the model to work through the problem before giving the answer. It helps most with maths, logic, multi-step planning and decisions with trade-offs.
- **Reasoning models** think internally before replying. You'll see features like "thinking" or "extended thinking" in AI apps. Turn them on for hard problems. For simple questions they're slower without being better.
- **Decomposition:** split a big question into smaller ones and answer them in order. "Should I take this job?" becomes: money, growth, commute, people, risk, then a verdict.
- **Self-checking:** ask the model to verify its answer. For example, plug the result back into the problem, or look for a counter-example.
- **Answer format:** ask for the reasoning first and a clearly separated final answer last, so it's easy to find.

## To-do

- [ ] Read the Learn section
- [ ] Do exercises 1 to 4
- [ ] Journal

## Exercises

**1. Napkin or no napkin.** In two fresh chats:

```text
A shop sells a phone for KES 24,000 after a 20% discount. It then raises the discounted price by 20%. What is the final price, and is it higher or lower than the original price? Answer with just the number and "higher" or "lower".
```

```text
A shop sells a phone for KES 24,000 after a 20% discount. It then raises the discounted price by 20%. What is the final price, and is it higher or lower than the original price? Work through it step by step, check your answer, then give the final answer on its own line.
```

(The correct final price is KES 28,800, which is lower than the original KES 30,000.) Did the quick version get it right?

**2. Break down a real decision.**

```text
I earn KES 85,000 a month. Rent is 25,000, I send 10,000 home, and I want to save for a KES 400,000 car in 18 months.

Work through this step by step: what's left each month, whether the goal is realistic, and 2 changes that would make it easier. Show your working, then give a one-line verdict.
```

Swap in your own numbers, or a friend's.

**3. Structured decomposition.** Pick a real decision you're facing (a course, a purchase, a job). Ask:

```text
Help me decide: [your decision].
First list the 5 factors that matter most for someone in my situation: [2 lines about you].
Then score each option on each factor from 1 to 5, with one sentence of reasoning per score.
Then give a recommendation, and tell me what information would change your mind.
```

**4. Make it check itself.** Ask any AI a logic puzzle, then follow up:

```text
Now try to prove your answer wrong. Look for a counter-example or a mistake in your reasoning. If you find one, correct it.
```

## Stretch

If your AI app has a thinking or reasoning mode, run exercise 3 with it on and off. Compare the quality, and how long each version took.

## Check yourself

1. Which kinds of task benefit most from step-by-step reasoning?
2. Why ask for the final answer on its own line?
3. When is a reasoning model *not* worth it?

<details>
<summary>Answers</summary>

1. Maths, logic, multi-step planning, and decisions with trade-offs.
2. So you (or a program) can find it easily, separated from the working.
3. For simple, factual or creative tasks, where it adds time and cost without improving the answer.

</details>

## Journal

*What decision am I currently making that deserves a napkin?*
