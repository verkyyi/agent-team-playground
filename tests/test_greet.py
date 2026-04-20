import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from greet import greet, farewell


def test_greet_returns_hello_with_name():
    assert greet("world").startswith("Hello, world")


def test_farewell_returns_goodbye_with_name():
    assert farewell("world") == "Goodbye, world!"
    assert farewell("Alice") == "Goodbye, Alice!"
