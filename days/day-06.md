# Day 6: Output that computers can read

**Level 2 · Techniques** · about 60 minutes · light technical

> Brian is building a little app that photographs receipts and turns them into a spending tracker. The AI reads the receipt perfectly. Then it replies: "Sure! Here's what I found 😊" followed by the data. His code expects pure data, gets a smiley face, and crashes.
>
> Welcome to structured output: getting answers in a shape that other programs, spreadsheets or people can use without cleaning them up first.

## Today's goal

Get reliable tables, templates and JSON, and know what to do when data is missing.

## Learn

- **Tables** for comparisons, **templates** for repeated documents, and **JSON** for anything a program will read.
- **JSON** is a text format for data: `{"name": "Amina", "age": 27}`. Almost every app and API speaks it.
- **Give the exact shape.** Write out the field names, types, and an example. Don't just say "give me JSON".
- **Plan for missing data.** Say what to do when a value isn't there (use `null`), or the model will invent something.
- **Say "only JSON, no other text".** Chat models love adding friendly sentences.
- **Developer tip:** many APIs now offer *structured outputs*, where the API itself guarantees the reply matches your schema. Use that feature in real apps, and prompt instructions in chat apps. You'll meet the API on Day 9.

## To-do

- [ ] Read the Learn section
- [ ] Do exercises 1 to 4
- [ ] Open one JSON output in a JSON validator (search "JSON validator" online) to check it's valid
- [ ] Journal

## Exercises

**1. Receipt to JSON.**

```text
Extract the data from this receipt. Reply with ONLY valid JSON, no other text, matching:
{"shop": string, "date": "YYYY-MM-DD", "items": [{"name": string, "price": number}], "total": number}
If a value is unreadable, use null.

Receipt: Naivas Westlands 14/03/2026 Milk 1L 65.00 Bread 60.00 Eggs x12 390.00 TOTAL 515.00
```

Paste the result into a JSON validator. Did it pass? Is the date in the right format?

**2. Test the missing-data rule.** Run exercise 1 again, but delete the date from the receipt. Did it use `null`, or did it invent a date? Then remove the "use null" line from the prompt and try again.

**3. A comparison table.**

```text
Compare 3 ways to learn Python as a complete beginner in Kenya: a free online course, a paid bootcamp, and a university short course.
Reply as a markdown table with columns: Option | Typical cost (KES) | Time per week | Best for | Biggest drawback.
After the table, one sentence recommending one option for a working adult with 5 hours a week.
```

Paste the table into Google Sheets or Excel. Did it land in proper columns?

**4. A reusable template.** Create a prompt that turns messy meeting notes into this exact template:

```text
## Meeting: [title], [date]
**Decisions:**
- ...
**Action items:**
| Who | What | By when |
**Open questions:**
- ...
```

Test it on some real (or invented) messy notes. Use the words "follow this template exactly".

## Stretch

Write a prompt that turns 10 lines of messy contact info ("john - 0712xxx - john at gmail dot com - met at devfest") into clean CSV. Import it into a spreadsheet.

## Check yourself

1. What should the prompt say about missing values, and why?
2. Why is "give me JSON" not enough?
3. What's the more reliable, API-level way to get JSON in real software?

<details>
<summary>Answers</summary>

1. Say exactly what to use, such as `null`. Otherwise the model may make up a plausible value.
2. You need the exact field names, types and format, and to forbid extra text. Otherwise the output varies each time.
3. The API's structured outputs feature, which enforces a schema.

</details>

## Journal

*What information do I keep retyping or copying between apps that AI could structure for me?*
