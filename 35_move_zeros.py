
def move_zeros(numbers):
    result = []

    for num in numbers:
        if num != 0:
            result.append(num)

    zero_count = len(numbers) - len(result)

    for i in range(zero_count):
        result.append(0)

    return result
