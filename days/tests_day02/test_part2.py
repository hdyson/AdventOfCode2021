from day02 import part2


INPUT_DATA = [
    "forward 5",
    "down 5",
    "forward 8",
    "up 3",
    "down 8",
    "forward 2",
]


def test_end_to_end() -> None:
    expected = 900

    actual = part2(INPUT_DATA)

    assert actual == expected
