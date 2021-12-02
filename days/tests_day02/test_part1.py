import days
from days.day02 import part1, parse_line


INPUT_DATA = [
    "forward 5",
    "down 5",
    "forward 8",
    "up 3",
    "down 8",
    "forward 2",
]


def test_parse_line() -> None:
    expected = ("forward", 5)

    actual = parse_line("forward 5")

    assert actual == expected


def test_end_to_end() -> None:
    expected = 150

    actual = part1(INPUT_DATA)

    assert actual == expected
