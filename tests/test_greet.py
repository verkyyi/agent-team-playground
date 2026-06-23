import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from greet import greet, greet_20260420183227


def test_greet_returns_hello_with_name():
    assert greet("world").startswith("Hello, world")


def test_greet_20260420183227():
    assert greet_20260420183227("world") == "Hello from e2e, world!"
