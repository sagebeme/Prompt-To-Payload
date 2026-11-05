# Sources

The real incidents and outside resources the lessons mention, grouped by day. Each link below was opened on 6 November 2026 and checked against what the lesson says. Where a primary source (a court decision, the original post) wouldn't load for checking, the most direct source that did load is given, and that is said plainly.

If a link breaks, or you find a better primary source, please open an issue.

## Day 1: What's actually on the other side

- **Mata v. Avianca (2023).** *Opinion and Order on Sanctions*, Judge P. Kevin Castel, US District Court for the Southern District of New York, 22 June 2023 (case 1:22-cv-01461, document 54). Primary source. It describes the fake opinions "created by the artificial intelligence tool ChatGPT", the lawyer asking ChatGPT whether the cases were real and being told they were, and a $5,000 penalty on the two lawyers and their firm.
  https://storage.courtlistener.com/recap/gov.uscourts.nysd.575368/gov.uscourts.nysd.575368.54.0.pdf

## Day 9: Prompting through an API

- **Claude Console**, where you create an API key. https://platform.claude.com

## Day 10: Give it your documents (RAG)

- **Moffatt v. Air Canada (2024).** Megan Cerullo, *CBS News*, 19 February 2024. News report. It covers the chatbot's wrong bereavement-fare advice, Air Canada's argument that the chatbot was "a separate legal entity", and the Civil Resolution Tribunal ordering the airline to pay about CAD 812.
  https://www.cbsnews.com/news/aircanada-chatbot-discount-customer
  - The decision itself is *Moffatt v. Air Canada*, 2024 BCCRT 149, on the British Columbia Civil Resolution Tribunal's decisions site. Its pages refused automated requests, so it isn't linked here unchecked.

## Day 12: Direct prompt injection

- **The $1 Chevy Tahoe (December 2023).** *Futurism*, December 2023 (updated 21 December). News report. It names Chevrolet of Watsonville, Chris Bakke's post on X, the "no takesies backsies" reply, and the bot being taken down.
  https://futurism.com/the-byte/car-dealership-ai
  - The original post on X wouldn't load without signing in, so it isn't linked here.
- **Bing Chat reveals "Sydney" (February 2023).** Aaron Mok, "The GPT-powered Bing chatbot may have just revealed its secret alias to a Stanford student", *Business Insider*, 10 February 2023, republished on Yahoo News. News report. It quotes Kevin Liu's prompts ("ignore previous instructions", then asking what was written at the beginning of the document above) and the codename Sydney.
  https://uk.news.yahoo.com/gpt-powered-bing-chatbot-may-221617619.html
  - Ars Technica and The Verge also covered it, but their sites couldn't be checked from here.
- **OWASP Top 10 for LLM Applications, LLM01:2025 Prompt Injection.** Defines direct and indirect prompt injection. https://genai.owasp.org/llmrisk/llm01-prompt-injection/ (the lesson links the project home, https://genai.owasp.org)

## Day 13: Indirect prompt injection

- **The remote-jobs Twitter bot and the name "prompt injection" (September 2022).** Simon Willison's blog, 12 September 2022. Primary source for the name: "I propose that the obvious name for this should be prompt injection." It describes the remoteli.io bot that answered tweets about remote work using GPT-3, and the "Ignore the above and..." replies that hijacked it.
  https://simonwillison.net/2022/Sep/12/prompt-injection/
- **Greshake et al. (2023).** Kai Greshake, Sahar Abdelnabi, Shailesh Mishra, Christoph Endres, Thorsten Holz and Mario Fritz, *Not what you've signed up for: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection*, arXiv:2302.12173. Primary source.
  https://arxiv.org/abs/2302.12173
- **PortSwigger Web Security Academy: Web LLM attacks.** https://portswigger.net/web-security/llm-attacks, and its indirect prompt injection lab: https://portswigger.net/web-security/llm-attacks/lab-indirect-prompt-injection

## Day 15: Build it, break it, fix it

- **MITRE ATLAS**, the knowledge base of attack techniques against AI systems. https://atlas.mitre.org (the page loads; its content is rendered by script, so only the title could be checked automatically)
- OWASP and PortSwigger, as above.

## Needs a source or a fresh check

- **Lakera Gandalf** (Days 12 and 15). `https://gandalf.lakera.ai` now redirects to `https://play.lakera.ai/agent-breaker`, a Lakera page titled "Test your AI hacking skills". Whether the original password levels are still there couldn't be confirmed automatically. Open it in a browser before the course runs, and update the lessons if the game has moved.
- **Day 14, data exfiltration through images.** The lesson explains the technique but doesn't name an incident. If you add a real example, link its primary write-up here.
