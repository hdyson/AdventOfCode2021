"""Some common utility functions."""
from typing import Iterator


def load(filename: str) -> Iterator[str]:
    """Return each line from the input as a string.

    Parameters
    ----------

    filename : str

    Yields
    ------

    : iterator of str
    """
    with open(filename) as file_handle:
        for line in file_handle.readlines():
            yield line.strip()
