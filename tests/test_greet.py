import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from greet import greet, greet_manual_20260423071904


def test_greet_returns_hello_with_name():
    assert greet("world").startswith("Hello, world")


def test_greet_manual_20260423071904():
    assert greet_manual_20260423071904("world") == "Hello manual dispatch, world!"
