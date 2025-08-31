def convert2decimal(x: str) -> int:
    result = 0
    n = len(x)
    for i in range(0, n):
        number = 2 ** (n - i - 1) * int(x[i])
        result = result + number
    return result
