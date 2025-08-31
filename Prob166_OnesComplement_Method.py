def scomplement(num):
    remainder = 0
    result = []
    while num != 0:
        remainder = num % 2
        result.append(remainder)
        num = num // 2

    # Manual reversing using swapping
    left = 0
    right = len(result) - 1
    while left < right:
        result[left], result[right] = result[right], result[left]
        left += 1
        right -= 1

    # One's complement
    for i in range(len(result)):
        if result[i] == 0:
            result[i] = 1
        else:  # instead of another if
            result[i] = 0

    return result

sc = scomplement(1000)
print(sc)
