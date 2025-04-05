"""Dictionary Construction in class COMP110!"""

__author__: str = "730715920"


def invert(d: dict[str, str]) -> dict[str, str]:
    """Inverts a dictionary, raise KeyError for duplicated values."""
    inverted: dict[str, str] = {}
    for key in d:
        value = d[key]
        if value in inverted:
            raise KeyError
        else:
            inverted[value] = key
    return inverted


# print(invert({"a": "z", "b": "y", "c": "x"}))
# print(invert({"apple": "cat"}))
# print(invert({"kris": "jordan", "michael": "jordan"}))


def count(values: list[str]) -> dict[str, int]:
    """Return a dictionary with the count of each unique string."""
    result: dict[str, int] = {}
    for item in values:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result


def favorite_color(favorites: dict[str, str]) -> str:
    """
    Returns the color that appears most frequently in the input dictionary.
    In case of a tie, returns the first color encountered.
    """
    color_counts: dict[str, int] = {}

    for name in favorites:
        color = favorites[name]
        if color in color_counts:
            color_counts[color] += 1
        else:
            color_counts[color] = 1

    max_color: str = ""
    max_count: int = 0

    for color in color_counts:
        if color_counts[color] > max_count:
            max_color = color
            max_count = color_counts[color]

    return max_color


def bin_len(words: list[str]) -> dict[int, set[str]]:
    """
    Bins a list of strings into a dictionary. The length of a string is the key
    and a set of strings of that length the value .
    """
    result: dict[int, set[str]] = {}
    for word in words:
        length = len(word)
        if length in result:
            result[length].add(word)
        else:
            result[length] = {word}
    return result
