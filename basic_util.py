
def round1(x: float) -> float:
    """Round to 1 decimal place."""
    return round(x, 1)


def mean(x: list[float]) -> float:
    return sum(x) / len(x)


def count(list, x):
    """Return the number of times `x` appears in `list`."""
    return sum(1 for y in list if y == x)

