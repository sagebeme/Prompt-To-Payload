# Day 4: Show, don't tell

**Level 2 · Techniques** · about 60 minutes · no coding

> Wanjiru runs social media for a small skincare brand. She spent ten minutes explaining the brand's "voice" to an AI: "fun but not childish, confident but warm, a bit cheeky." Every caption it wrote sounded like a bank advert.
>
> Then she pasted three of her old captions and wrote "write like these." The next caption was so close to her style that her manager asked when she'd written it.
>
> Examples beat explanations. That's true for new employees, and it's true for AI.

## Today's goal

Use examples (few-shot prompting) to teach tone, format and judgement, and avoid the traps that come with them.

## Learn

- **Zero-shot** means no examples, just instructions. **Few-shot** means you include 2 to 5 examples of input and the output you want.
- Examples teach several things at once: format, length, tone, and the judgement calls that are hard to put into words.
- **Trap 1: over-copying.** Models copy examples closely. If all your examples start with "Hey!", every output will too. Vary them on purpose.
- **Trap 2: bias.** If 4 of your 5 examples are labelled "positive", the model leans positive. Balance your examples across the answers you expect.
- **Negative examples** mark the line: "Here's one that's too formal: ... Don't write like this."
- Mark examples clearly, for instance with `Example 1:` labels or `<example>` tags, so they're not confused with the real task.

## To-do

- [ ] Read the Learn section
- [ ] Do exercises 1 to 4
- [ ] Add your best few-shot prompt to your library
- [ ] Journal

## Exercises

**1. A classifier in one prompt.**

```text
Classify each customer message as URGENT, NORMAL or IGNORE.

"My payment went through twice, please help" → URGENT
"Do you deliver to Kisumu?" → NORMAL
"🔥🔥🔥 follow me for crypto tips" → IGNORE

Now classify:
"The app logged me out and I can't reset my password"
"Love your new colours!"
"You charged me but my order never arrived, it's been 2 weeks"
"hi"
```

Did it agree with how you'd label them? Which one was hardest?

**2. Teach your voice.** Find three things you've written: messages, posts or emails. Then:

```text
Here are 3 examples of how I write:

Example 1: """..."""
Example 2: """..."""
Example 3: """..."""

In the same voice, write a message inviting my team to a Friday lunch to celebrate finishing a big project. Don't copy phrases from the examples, just the style.
```

Ask a friend to guess which message is the AI's.

**3. Break it on purpose.** Redo exercise 1, but make every example URGENT. Then classify "Do you have this in blue?". Did it over-label as urgent? That's example bias.

**4. Negative example.** Ask for a product description of a phone case. Then add:

```text
Here is an example of what I DON'T want: "Elevate your style with this revolutionary, game-changing case that redefines protection!" It's full of hype words. Rewrite it plainly, like a friend recommending it.
```

## Stretch

Build a few-shot "tone translator" that turns angry customer complaints into calm, factual summaries for your manager. Test it on 5 complaints you write yourself, including one sarcastic one.

## Check yourself

1. What's the difference between zero-shot and few-shot?
2. Your outputs all start with the same phrase. Why?
3. Why balance the labels across your examples?

<details>
<summary>Answers</summary>

1. Zero-shot gives only instructions. Few-shot also includes worked examples of input and output.
2. Your examples probably all start that way, and the model is copying them. Vary the openings.
3. Unbalanced examples bias the model toward whichever label appears most.

</details>

## Journal

*Which task in my life would be easier to teach with examples than with instructions?*
