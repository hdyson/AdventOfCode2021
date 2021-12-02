#!/usr/bin/env python
"""Launcher to run all days of advent of code 2021."""
from common import load_integers
import day01
import day02


def main() -> None:
    day_1_input = list(load_integers("./inputs/day01.txt"))
    day_1_part_1_result = day01.part1(day_1_input)
    day_1_part_2_result = day01.part2(day_1_input)
    print(f"day 1 part 1: {day_1_part_1_result} day 1 part 2: {day_1_part_2_result}")

    day_2_input = list(load_integers("./inputs/day02.txt"))
    day_2_part_1_result = day02.part1(day_2_input)
    day_2_part_2_result = day02.part2(day_2_input)
    print(f"day 2 part 1: {day_2_part_1_result} day 2 part 2: {day_2_part_2_result}")


if __name__ == "__main__":
    main()
