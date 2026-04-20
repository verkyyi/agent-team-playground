import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from greet import greet


def test_greet_returns_hello_with_name():
    assert greet("world").startswith("Hello, world")
