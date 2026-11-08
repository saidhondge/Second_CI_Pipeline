def find_missing_number(numbers):
    n = len(numbers) + 1

    result = 0

    for i in range(1, n + 1):
        result ^= i

    for num in numbers:
        result ^= num

    return result


if __name__ == "__main__":
    print(find_missing_number([1, 2, 4, 5]))