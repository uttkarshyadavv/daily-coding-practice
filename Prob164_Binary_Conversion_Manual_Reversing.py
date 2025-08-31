def binary_conversion(num: int) -> str:
    remainder = 0
    result = []
    while num != 0:
        remainder = num % 2
        result.append(remainder)
        num = num // 2

    # Manual reversing using swapping (your way)
    left = 0
    right = len(result) - 1
    while left < right:
        result[left], result[right] = result[right], result[left]
        left += 1
        right -= 1
