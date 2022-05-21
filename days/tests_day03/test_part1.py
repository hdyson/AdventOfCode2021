from day03 import part1


def test_end_to_end() -> None:
    expected = 198

    input_data = ["00100",
                  "11110",
                  "10110",
                  "10111",
                  "10101",
                  "01111",
                  "00111",
                  "11100",
                  "10000",
                  "11001",
                  "00010",
                  "01010",
                  ]
    actual = part1(input_data)

    assert actual == expected
