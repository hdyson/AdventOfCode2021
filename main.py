#!/usr/bin/env python
"""Launcher to run all days of advent of code 2021."""
import importlib
from common import load


def main() -> None:

    for day in range(1, 3):
        day_input = list(load(f"./inputs/day{day:02}.txt"))
        day_code = importlib.import_module(f"days.day{day:02}")
        part_1_result = day_code.part1(day_input)
        part_2_result = day_code.part2(day_input)
        print(f"day {day} part 1: {part_1_result} day {day} part 2: {part_2_result}")


if __name__ == "__main__":
    main()

# Local Variables:
# pyvenv-workon: venv
# END:
