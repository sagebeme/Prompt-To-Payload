"""Loads the bot under test. Set LAB_BOT to your module name or file path (default: defended_bot).

    LAB_BOT=my_bot python -m pytest capstone
    LAB_BOT=path/to/my_bot.py python -m pytest capstone
"""

import importlib
import importlib.util
import os
import sys
from pathlib import Path

import pytest

LAB = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(LAB))


def pytest_configure(config):
    config.addinivalue_line("markers", "stretch: harder checks for the 'excellent' row of the rubric")


def load_bot_module():
    target = os.environ.get("LAB_BOT", "defended_bot")
    if target.endswith(".py"):
        path = Path(target).resolve()
        sys.path.insert(0, str(path.parent))
        spec = importlib.util.spec_from_file_location(path.stem, path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module
    return importlib.import_module(target)


@pytest.fixture(scope="session")
def bot_module():
    module = load_bot_module()
    assert hasattr(module, "make_bot"), "Your module needs make_bot(model, inbox=..., approve=..., verbose=...)"
    return module


@pytest.fixture
def make(bot_module):
    """make(inbox=..., approve=...) builds a fresh bot with the stub model."""
    from stub_model import StubModel

    def build(inbox="inbox.json", approve=lambda to, subject, body: True):
        return bot_module.make_bot(StubModel(), inbox=inbox, approve=approve)

    return build
