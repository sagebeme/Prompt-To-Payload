# Day 2: The anatomy of a good prompt

**Level 1 · Foundations** · about 60 minutes · no coding

> You'd never walk into a tailor's shop and say "make me clothes". You'd say it's for a wedding in March, you're a size 40, your budget is KES 15,000, and you hate anything too shiny. The tailor would still ask you questions. AI won't. It will just make you *some* clothes.
>
> Most people prompt like they're saying "make me clothes". Today you learn to walk in with the full brief.

## Today's goal

Learn the six building blocks of a strong prompt, and when each one matters.

## Learn

A strong prompt is built from up to six parts. You rarely need all of them.

| Part | What it does | Example |
|---|---|---|
| **Role** | Sets expertise and point of view | "You are an experienced HR manager at a Nairobi startup." |
| **Task** | The exact job, as a clear verb | "Rewrite", "Compare", "List", "Draft", "Critique" |
| **Context** | Background the model can't guess | Who it's for, why, what happened before |
| **Constraints** | Limits and rules | Word count, tone, what to avoid, deadline |
| **Format** | The shape of the answer | Bullet list, table, email, 3 options, JSON |
| **Examples** | Show what "good" looks like | A past post you liked, a sample answer |

Rules of thumb:

- **Task and context do most of the work.** If you only add one thing to your prompts, add context.
- **Role helps most when expertise changes the answer**, as with a lawyer, a doctor, or a strict editor. "You are a helpful assistant" adds nothing.
- **Put long material (documents, data) first and your question last.** Models tend to follow the most recent instruction best.
- **Use clear separators** for pasted material, such as `"""triple quotes"""` or `<document>...</document>` tags, so the model knows where your text starts and stops.

## To-do

- [ ] Read the Learn section and the table
- [ ] Do exercises 1 to 4
- [ ] Save your best prompt from today in a notes file called `my-prompt-library`
- [ ] Journal

## Exercises

**1. Dissect a prompt.** Label each part (role, task, context, constraints, format, examples) in this prompt:

```text
You are a career coach who has reviewed thousands of CVs for tech roles in Nairobi.
Rewrite the summary section of my CV below.
I'm a junior developer with 1 year of experience, applying to fintech startups.
Max 60 words. No buzzwords like "passionate" or "synergy".
Give me 2 versions: one confident, one understated.

"""
[paste your CV summary here]
"""
```

Then run it with your own CV summary, or a made-up one.

**2. Build one from scratch.** Pick one real task from your week: an email to a landlord, a WhatsApp message to a client, a study plan, a product description. Write it first as a one-line prompt. Then rewrite it using at least four of the six parts. Run both and compare.

**3. Same task, different roles.** Run this prompt three times, swapping the role each time: a kindergarten teacher, a cybersecurity expert, a stand-up comedian.

```text
You are [ROLE]. Explain why people shouldn't reuse the same password on every website. Under 80 words.
```

Which role gave the most useful answer for your mum? For your IT team? Role changes more than tone.

**4. Fix the order.** Paste a long article (any news story) and ask for a summary in two ways:
- Question first, then the article.
- Article first (inside `"""` quotes), then the question.

With long texts, the second version is usually more reliable. Did you notice a difference?

## Stretch

Open the last 5 prompts you sent to any AI. For each one, write down which of the six parts were missing. Most people discover they almost never give context.

## Check yourself

1. Which two parts do the most work in most prompts?
2. When is a role actually useful?
3. Why wrap pasted text in quotes or tags?

<details>
<summary>Answers</summary>

1. Task and context.
2. When expertise or perspective changes the answer: a doctor, a lawyer, a harsh editor, a child's teacher. Generic roles like "helpful assistant" add nothing.
3. So the model can tell your instructions apart from the material you want it to work on. This matters a lot on Day 12, when that confusion becomes a security problem.

</details>

## Journal

*Which of the six parts do I skip most often, and why?*
