arr = [4, 1, 2, 1, 2]

single = 0
for num in arr:
    single ^= num  # XOR cancels out duplicates

print(single)  # 4
