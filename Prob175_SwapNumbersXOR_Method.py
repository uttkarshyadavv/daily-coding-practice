a = 5  # 0101
b = 9  # 1001

a = a ^ b
b = a ^ b
a = a ^ b

print(a, b)  # a = 9, b = 5
