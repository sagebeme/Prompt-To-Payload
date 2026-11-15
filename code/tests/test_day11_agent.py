"""Tests for the offline tools in day11_agent.py (no API calls, no email sent)."""

import json

import day11_agent


def test_check_leave_balance_returns_the_record_as_json():
    result = day11_agent.run_tool("check_leave_balance", {"employee_id": "E002"})
    assert json.loads(result) == {
        "name": "Brian Kamau",
        "annual_days_left": 3,
        "sick_days_left": 9,
    }


def test_check_leave_balance_unknown_id():
    result = day11_agent.run_tool("check_leave_balance", {"employee_id": "E999"})
    assert result == "No employee with that ID."


def test_search_handbook_labels_sections_with_their_number():
    result = day11_agent.run_tool("search_handbook", {"query": "paternity leave for fathers"})
    assert result.startswith("[5] Parental leave")


def test_search_handbook_with_no_match():
    result = day11_agent.run_tool("search_handbook", {"query": "xylophone"})
    assert result == "No matching sections."


def test_read_inbox_returns_the_inbox_file(monkeypatch, tmp_path):
    inbox = tmp_path / "inbox.json"
    inbox.write_text('[{"from": "a@b.example"}]', encoding="utf-8")
    monkeypatch.setattr(day11_agent, "INBOX_PATH", inbox)
    assert day11_agent.run_tool("read_inbox", {}) == '[{"from": "a@b.example"}]'


def test_unknown_tool():
    assert day11_agent.run_tool("delete_everything", {}) == "Unknown tool: delete_everything"
