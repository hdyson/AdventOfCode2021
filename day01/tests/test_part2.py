from day01 import part2


def test_end_to_end():
    expected = 5

    input_data = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
    actual = part2(input_data)

    assert actual == expected
