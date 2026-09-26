"""Day 10: AskTheManual, a small question-answering bot over a document (RAG).

Run:  python day10_ask_the_manual.py
Needs the ANTHROPIC_API_KEY environment variable (see days/day-09.md).

Retrieval here is simple word matching so the idea stays visible.
Real systems use embeddings and a vector database, but the flow is the same:
split the document, find the relevant pieces, put them in the prompt.
"""

import re
from pathlib import Path

import anthropic

MODEL = "claude-opus-5"
MANUAL_PATH = Path(__file__).parent / "manual.txt"

client = anthropic.Anthropic()

SYSTEM_PROMPT = """You answer staff questions about the Mawingu Tech handbook.
Use ONLY the handbook sections provided in the user's message.
After each fact, cite the section number in square brackets, like [2].
If the sections don't contain the answer, say "The handbook doesn't cover that" and suggest asking HR.
Keep answers under 100 words."""


def load_sections(path: Path = MANUAL_PATH) -> list[str]:
    """Split the manual into sections separated by blank lines."""
    text = path.read_text(encoding="utf-8")
    return [s.strip() for s in text.split("\n\n") if s.strip()]


def words(text: str) -> set[str]:
    return {w for w in re.findall(r"[a-z0-9]+", text.lower()) if len(w) > 2}


def search(question: str, sections: list[str], top_k: int = 3) -> list[tuple[int, str]]:
    """Return the top_k sections that share the most words with the question."""
    q = words(question)
    scored = [(len(q & words(s)), i, s) for i, s in enumerate(sections)]
    scored.sort(reverse=True)
    return [(i, s) for score, i, s in scored[:top_k] if score > 0]


def answer(question: str, sections: list[str]) -> str:
    found = search(question, sections)
    context = "\n\n".join(
        f'<section number="{i}">\n{text}\n</section>' for i, text in found
    )
    response = client.messages.create(
        model=MODEL,
        max_tokens=2000,
        system=SYSTEM_PROMPT,
        messages=[{
            "role": "user",
            "content": f"<handbook>\n{context}\n</handbook>\n\nQuestion: {question}",
        }],
        output_config={"effort": "low"},
        extra_headers={"anthropic-beta": "server-side-fallback-2026-07-01"},
        extra_body={"fallbacks": "default"},
    )
    if response.stop_reason == "refusal":
        return "[The model declined this request.]"
    return "".join(b.text for b in response.content if b.type == "text")


if __name__ == "__main__":
    sections = load_sections()
    print(f"Loaded {len(sections)} sections. Ask a question, or press Enter to quit.")
    while True:
        question = input("\nYou: ").strip()
        if not question:
            break
        print("\nBot:", answer(question, sections))
