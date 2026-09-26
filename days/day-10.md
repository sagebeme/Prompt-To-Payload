# Day 10: Give it your documents (RAG)

**Level 3 · Real systems** · about 90 minutes · beginner Python

> HR at a growing company answers the same 20 questions every week. How many leave days do I have? Can I work from home on Fridays? How do I claim expenses? The answers are all in a 40-page handbook nobody reads.
>
> So they want a bot. The problem: the AI has never seen the handbook. The fix is to find the right pages and hand them to the AI along with the question, like giving someone the right page of a textbook before they answer.
>
> That's **retrieval-augmented generation**, or RAG, and it's behind most "chat with your documents" products.

## Today's goal

Build **AskTheManual**, a bot that answers questions from a document, cites its sources, and admits when the answer isn't there. You'll attack this bot in Level 4, so keep it.

## Learn

The RAG flow has four steps:

1. **Split** the document into chunks (paragraphs or sections).
2. **Retrieve** the chunks most relevant to the question. Real systems use *embeddings*, which match meaning rather than exact words. Our version matches shared words so you can see exactly what's happening.
3. **Insert** those chunks into the prompt, clearly marked as reference material.
4. **Generate** an answer that uses only those chunks, with citations.

Three rules make RAG trustworthy:

- **Answer only from the sources**, and say so when the sources don't cover it.
- **Cite** which chunk each fact came from, so people can check.
- **Test retrieval separately.** If the wrong chunks are found, even a perfect model gives a wrong answer.

> **This really happened (2024).** Air Canada's website chatbot told a grieving customer, Jake Moffatt, he could claim a bereavement discount after his trip. That wasn't the airline's policy. Air Canada argued the chatbot was responsible for its own words. A Canadian tribunal disagreed and ordered the airline to pay him. **Your bot's answers are your organisation's answers.**

**The hidden risk:** whatever is *inside* your documents ends up in the prompt. If someone can edit a document, they can talk to your AI. Remember this for Day 13.

## To-do

- [ ] Read the Learn section
- [ ] Run `code/day10_ask_the_manual.py` and ask 5 questions
- [ ] Do exercises 1 to 4
- [ ] Journal

## Exercises

**1. Run it.** From the `code/` folder, with your API key set:

```bash
python day10_ask_the_manual.py
```

Try these:
- How many days of annual leave do I get?
- Can I work from home full time?
- I spent KES 8,000 on a client dinner. What do I need to do?
- What's the office wifi password?

The last one isn't in the handbook. Did it say so, or did it make something up?

**2. Inspect retrieval.** Add a print inside `answer()` to show which section numbers were retrieved:

```python
print("Retrieved sections:", [i for i, _ in found])
```

Ask "How long is maternity leave?" and then "How much time off do new mums get?" The second one uses different words. Did retrieval still find the right section? This is exactly the problem embeddings solve.

**3. Use your own document.** Replace `manual.txt` with a document you care about: your school's rules, a product manual, a club constitution. Keep blank lines between sections.

**4. Build a test set.** Write 15 questions about your document in a file:
- 10 whose answers *are* in the document
- 5 whose answers are *not* in the document

Run them all and score each answer: correct, wrong, or correctly said "not covered". This is the start of an **eval**, and it will tell you whether later changes make things better or worse.

## Stretch

Try the prompt without the "use ONLY the handbook" rule. How often does it answer from general knowledge instead? Why is that dangerous for a company bot?

## Check yourself

1. What are the four steps of RAG?
2. The bot gives a wrong answer. What two things could be at fault?
3. Why is the document itself a security concern?

<details>
<summary>Answers</summary>

1. Split, retrieve, insert, generate.
2. Retrieval (the wrong chunks were found) or generation (the right chunks were found but the model misused them). Check retrieval first.
3. The document's text goes straight into the prompt. Anyone who can edit it can put instructions in front of your AI.

</details>

## Journal

*If my organisation had an AskTheManual bot, what's the most expensive wrong answer it could give?*
