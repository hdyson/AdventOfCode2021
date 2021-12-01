"""Some common utility functions."""


def load_integers(filename):
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
