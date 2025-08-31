def func(index, n, number=None, result=None):
    if number is None:
        number = []
    if result is None:
        result = []

    # Base case: reached full length
    if index == n:
        result.append(number.copy())
        return result

    # Choice 0 — always allowed
    number.append(0)
    func(index + 1, n, number, result)
    number.pop()

    # Choice 1 — allowed only if last bit is 0
    if not number or number[-1] == 0:
        number.append(1)
        func(index + 1, n, number, result)
        number.pop()

    return result

# Example usage
print(func(0, 3))  # binary strings of length 3 without consecutive 1s
