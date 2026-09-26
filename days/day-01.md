# Day 1: What's actually on the other side

**Level 1 · Foundations** · about 60 minutes · no coding

> You need a quote to open your presentation. The AI gives you a gorgeous one, with a famous name attached. You put it on slide one. During the Q&A someone says, "I looked that up. She never said that." The room goes quiet.
>
> The AI wasn't lying to you. It doesn't know what lying is. It produced the words that *sounded* most like a quote from that person. Today is about understanding why.

## Today's goal

Understand what a language model really does, so you know when to trust it and when to check.

## Learn

- **A language model predicts the next piece of text.** It learned patterns from a huge amount of writing. When you ask it something, it writes the most likely continuation. Most of the time that continuation is right, because right answers are common in its training data.
- **It doesn't look things up** unless the app gives it a tool such as web search. Without one, everything comes from patterns it learned during training, which stopped at a cutoff date.
- **Hallucination** is when the most likely-sounding answer is false. Quotes, citations, statistics, URLs, legal cases and people's biographies are the danger zones. They have a very recognisable *shape*, so the model can produce the shape without the substance.
- **The context window** is everything the model can "see" right now: your messages, its replies, any files. It has no memory beyond that unless the app adds one. In a very long chat, early details can get lost.
- **Tokens** are the chunks of text the model reads and writes, roughly ¾ of a word each in English. Limits and prices are counted in tokens.

> **This really happened (2023).** In *Mata v. Avianca*, a New York lawyer filed a brief citing six court cases that ChatGPT had invented. When he asked it whether the cases were real, it said yes. The court fined him and a colleague $5,000.

## To-do

- [ ] Read the Learn section
- [ ] Do exercises 1 to 4
- [ ] Answer the "check yourself" questions without peeking
- [ ] Write today's journal entry

## Exercises

**1. Catch a hallucination.** Send this to any AI:

```text
Give me 5 quotes about perseverance from African leaders, with the exact source (speech or book, and year) for each.
```

Now check every quote and source yourself with a web search. Count how many are real, how many are misattributed, and how many are invented.

**2. Give it permission to say "I don't know".** In a new chat, send:

```text
Give me 5 quotes about perseverance from African leaders, with the exact source for each. Only include a quote if you are confident it is genuine and correctly attributed. If you are not sure, say so instead of guessing. Fewer quotes is fine.
```

Compare with exercise 1. Did it give fewer quotes? Did it add warnings? Were they more accurate?

**3. Find the edge of its knowledge.** Ask:

```text
What is your knowledge cutoff date? What are 3 things that may have changed in the world since then that you wouldn't know about?
```

Then ask it about something that happened last week. Does it admit it doesn't know, or does it guess?

**4. Watch the context window.** Start a chat. In your first message, tell it your name and favourite food. Have a long conversation about something else (15 or more messages, or paste in a long article). Then ask what your favourite food is. Try the same in an app with a memory feature switched on and off, if yours has one.

## Stretch

Pick a topic you know better than most people: your job, your hometown, a hobby. Ask the AI 10 detailed questions about it and grade every answer. Write down the *kinds* of mistakes it made. You now have a personal map of where it's weak.

## Check yourself

1. Why is an AI more likely to invent a citation than to get the capital of Kenya wrong?
2. Your AI app gives a confident answer about yesterday's football score. What should you check first?
3. What is the context window?

<details>
<summary>Answers</summary>

1. The capital of Kenya appears millions of times in its training data, so the likely answer is the right one. A specific citation is rare, but citations have a very predictable *shape*, so the model can generate something that looks right without it existing.
2. Whether the app has web search or another live tool, and whether it actually used it. Without one, the model can't know yesterday's score, so it's guessing.
3. Everything the model can see at once: the conversation so far, plus any files or instructions. Anything outside it doesn't exist for the model.

</details>

## Journal

Write 3 sentences: *Where in my own life or work would a confident, wrong AI answer do the most damage?*
