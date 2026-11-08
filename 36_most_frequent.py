from collections import Counter


def most_frequent(items):
    """Return the most frequent element. On a tie, the first one to appear wins.
    Returns None for an empty list."""
    if not items:
        return None
    counts = Counter(items)
    highest = max(counts.values())
    for item in items:
        if counts[item] == highest:
            return item


if __name__ == "__main__":
    print(most_frequent([1, 3, 2, 3, 1, 3]))  # 3