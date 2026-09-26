# Prompt to Payload

A 15-day course that takes learners from everyday AI prompting to prompt injection, red-teaming and defence, taught through relatable stories, real public incidents and hands-on exercises.

## The programme

| Level | Days | Topics |
|---|---|---|
| **1 · Foundations** | 1–3 | How LLMs work, anatomy of a good prompt, specificity and iteration |
| **2 · Techniques** | 4–8 | Few-shot prompting, reasoning, structured output, system prompts, prompt chains |
| **3 · Real systems** | 9–11 | The Claude API in Python, RAG ("AskTheManual"), tools, agents and evals |
| **4 · Security** | 12–15 | Direct and indirect prompt injection, defence in depth, red-team capstone |

Each day in [`days/`](days/) has a story, a short lesson, a to-do checklist, exercises, a stretch task, self-check questions and a journal prompt. Days 1–8 need only an AI chat app. Days 9–14 use the Python scripts in [`code/`](code/).

## Repository layout

```
index.html        Course overview and 15-day map (the home page)
day.html          Lesson viewer: renders days/day-NN.md with saved to-do checkboxes
assets/days.js    Day titles and levels, shared by both pages
days/             One Markdown file per day (also readable directly on GitHub)
code/             Python exercises: API basics, RAG bot, agent, hardened agent
```

The site is plain static files. There is no build step and nothing to install.

## Run it locally

Browsers block pages opened straight from disk from loading the lesson files, so serve the folder:

```bash
python3 -m http.server 8000
```

Then open http://localhost:8000.

## Deploy it for students

Push this repo to GitHub, then pick any host. Each one gives you a public URL to share with students.

**Vercel**
1. vercel.com → Add New → Project → import this repository.
2. Leave Framework Preset as "Other" and the build settings empty. `vercel.json` already sets this.
3. Deploy.

**Render**
1. render.com → New → Blueprint → pick this repository. `render.yaml` sets up a free static site.
2. Or create a Static Site manually with build command `echo done` and publish directory `.`.

**Netlify**
1. app.netlify.com → Add new site → Import an existing project → pick this repository.
2. `netlify.toml` sets publish directory `.` with no build command.

**GitHub Pages**
1. Repository Settings → Pages → Deploy from a branch → `main`, folder `/ (root)`.
2. The site appears at `https://<username>.github.io/Prompt-To-Payload/`.

Every push to `main` redeploys automatically on all four.

Student progress (ticked to-dos) is saved in each student's own browser, so there are no accounts or database to manage.

## Running the Python exercises

```bash
cd code
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
export ANTHROPIC_API_KEY="your-key"
python day09_first_call.py
```

See [Day 9](days/day-09.md) for the full setup. Never commit API keys; `.env` files are already ignored.

## Ethics

Level 4 teaches attack techniques so people can defend against them. Only test systems you own or have written permission to test, practise on purpose-built labs, and report vulnerabilities privately. Day 12 opens with these rules and learners agree to them before starting.
