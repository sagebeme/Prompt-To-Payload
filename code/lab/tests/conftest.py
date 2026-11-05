"""Lets the tests import labbot, defended_bot and stub_model from code/lab/."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
