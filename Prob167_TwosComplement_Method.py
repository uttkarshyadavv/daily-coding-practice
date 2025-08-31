def scomplement(num):
    remainder = 0
    result = []

    # Decimal → binary (your way)
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

    # One's complement (flip bits)
    for i in range(len(result)):
        if result[i] == 0:
            result[i] = 1
        else:
            result[i] = 0

    # Two's complement (add 1 with carry, your loop style)
    carry = 1
    i = len(result) - 1
    while i >= 0 and carry == 1:
        if result[i] == 0:
            result[i] = 1
            carry = 0
        else:
            result[i] = 0
            carry = 1
        i -= 1

    return result

sc = scomplement(1000)
print(sc)
