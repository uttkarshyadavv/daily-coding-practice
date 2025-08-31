num = 11  # 1011
i = 1
num &= ~(1 << i)  # clears bit 1
print(num)  # 9 (1001)
