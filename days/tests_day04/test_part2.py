from day04 import part2


def test_end_to_end() -> None:
    expected = 230

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
    actual = part2(input_data)

    assert actual == expected
