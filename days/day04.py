#!/usr/bin/env python
"""Day 4 of Advent of Code."""
import itertools


class BingoBoard:
    rows = list()
    columns = list()
    seen_values = set()

    def __call__(self, number: int) -> bool:
        if len(self.seen_values) < 5:
            self.seen_values.add(number)
        else:
            already_called = set(itertools.permutations(self.seen_values, r=5))
            self.seen_values.add(number)
            for new_permutation in set(
                itertools.permutations(self.seen_values) - already_called
            ):
                for row in self.rows:
                    if new_permutation in row:
                        return True
                for column in self.columns:
                    if new_permutation in column:
                        return True
        return False


def part1(input_data: list[str]) -> int:
    numbers_to_call = (int(number) for number in input_data[0].split())

    columns = dict()
    rows = dict()
    boards = []
    board = None
    row_index = 0
    for row in input_data[1:]:
        if row == "":
            if board is not None:
                boards.append(board)
            board = BingoBoard()
            row_index = 0
        else:
            for column_index, value in enumerate(int(number) for number in row.split()):
                pass
                

def part2(input_data: list[str]) -> int:
    pass
