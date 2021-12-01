from day01 import part1


def test_end_to_end():
    expected = 7

    input_data = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
    actual = part1(input_data)

    assert actual == expected
