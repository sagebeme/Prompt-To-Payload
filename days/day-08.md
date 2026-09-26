# Day 8: Prompt chains

**Level 2 · Techniques** · about 90 minutes · no coding

> A restaurant kitchen doesn't have one chef doing everything at once. Someone preps, someone cooks, someone plates, and the head chef checks every dish before it leaves.
>
> Asking an AI to research, outline, write, edit and format in one giant prompt is one exhausted chef doing everything. Split it into stations and the quality jumps.

## Today's goal

Design a multi-step prompt chain for a real, repeated task, and finish the Level 2 lab.

## Learn

- A **prompt chain** is a series of prompts where each step's output becomes the next step's input.
- **Why chains work:**
  - each step has one clear job
  - you can check and fix the work between steps
  - you can reuse the steps that work well
- A common content chain: **research → outline → draft → critique → polish**.
- **Pass outputs cleanly.** Paste the previous output inside clear markers, such as `"""outline"""`, and say what to do with it.
- **Put a human checkpoint** where mistakes are expensive. Checking the outline before the draft saves rewriting the whole draft.
- Chains are the manual version of what AI agents do automatically. You'll build one on Day 11.

## To-do

- [ ] Read the Learn section
- [ ] Run the 5-step chain in exercise 1
- [ ] Design your own chain (exercise 2)
- [ ] Complete the Level 2 lab
- [ ] Journal

## Exercises

**1. Run a full chain.** Pick a topic you care about. Run each step in the same chat, reading each output before moving on.

Step 1: research

```text
I'm writing a 600-word blog post for young Kenyan professionals about [TOPIC].
List the 8 most important points, facts or arguments on this topic. Mark anything you're unsure about with (verify).
```

Step 2: outline

```text
Using only the points you listed, create an outline: a hook, 3 sections with 2 to 3 bullets each, and a conclusion with one clear action for the reader.
```

*(Checkpoint: edit the outline yourself before continuing.)*

Step 3: draft

```text
Here is my approved outline:
"""
[paste your edited outline]
"""
Write the full post, around 600 words. Conversational, like a smart friend talking. Short paragraphs.
```

Step 4: critique

```text
Act as a tough editor. List the 5 biggest problems with this draft: weak sentences, unclear claims, boring parts, anything that needs a source. Don't rewrite yet.
```

Step 5: polish

```text
Fix all 5 problems. Keep it under 650 words. Then give me 3 title options.
```

Compare the result to asking for "a 600-word blog post about [TOPIC]" in one prompt.

**2. Design your own chain.** Choose something you do every week: a newsletter, client reports, a study guide from lecture notes, social posts. Write out:
- the steps (3 to 5)
- the prompt for each step
- where your human checkpoint goes

## Level 2 lab: your personal content machine

1. Turn your chain from exercise 2 into saved templates, in a notes app or a Custom GPT, Project or Gem.
2. Run it on **three different inputs**.
3. For each run, note how many minutes of editing were still needed and what went wrong.
4. Improve the weakest step's prompt and run it once more.

Add the templates and your notes to your course portfolio.

## Check yourself

1. Give two reasons chains beat one big prompt.
2. Where should a human checkpoint go?
3. How do you pass one step's output into the next safely?

<details>
<summary>Answers</summary>

1. Each step has one clear job, you can check work between steps, and good steps are reusable.
2. Before the most expensive step to redo, or wherever an error would spread (for example, approve the outline before drafting).
3. Paste it inside clear markers (quotes or tags) and state exactly what to do with it.

</details>

## Journal

*Which step of my chain needed the most fixing, and why do I think that is?*
