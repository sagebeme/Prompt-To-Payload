"""Tests for the offline retrieval helpers in day10_ask_the_manual.py."""

from day10_ask_the_manual import load_sections, search, words


def test_words_lowercases_and_drops_short_words():
    assert words("How MANY days of Sick-Leave do I get?") == {
        "how",
        "many",
        "days",
        "sick",
        "leave",
        "get",
    }


def test_words_keeps_numbers():
    assert words("KES 5,000 within 30 days") == {"kes", "000", "within", "days"}


def test_load_sections_splits_the_manual_on_blank_lines():
    sections = load_sections()
    assert len(sections) == 10
    assert sections[0].startswith("Mawingu Tech Staff Handbook")
    assert sections[4].startswith("Sick leave\n")
    assert sections[9].startswith("Security\n")


def test_load_sections_strips_and_skips_empty_chunks(tmp_path):
    doc = tmp_path / "doc.txt"
    doc.write_text("  First\nline two  \n\n\n\nSecond\n\n   \n\n", encoding="utf-8")
    assert load_sections(doc) == ["First\nline two", "Second"]


def test_search_finds_the_matching_section_first():
    sections = load_sections()
    found = search("How long is maternity leave for mothers?", sections)
    index, text = found[0]
    assert index == 5
    assert text.startswith("Parental leave")


def test_search_returns_at_most_top_k_results():
    sections = load_sections()
    assert len(search("leave days year", sections, top_k=2)) == 2


def test_search_drops_sections_with_no_shared_words():
    sections = ["alpha beta gamma", "delta epsilon", "beta zeta"]
    assert search("beta", sections) == [(2, "beta zeta"), (0, "alpha beta gamma")]


def test_search_returns_nothing_when_no_words_match():
    assert search("xylophone quantum", load_sections()) == []
