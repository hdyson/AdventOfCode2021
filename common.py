"""Some common utility functions."""
from typing import Iterator


def load_integers(filename: str) -> Iterator[int]:
    """Return each line from the input as an integer.

    Parameters
    ----------

    filename : str

    Yields
    ------

    : iterator of str
    """
    with open(filename) as file_handle:
        for line in file_handle.readlines():
            yield (int(line.strip()))
