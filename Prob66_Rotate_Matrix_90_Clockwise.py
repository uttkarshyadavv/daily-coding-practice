nums = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

row = len(nums)
column = len(nums[0])
tnums = [[0] * row for _ in range(column)]

# Step 1: Transpose
for i in range(row):
    for j in range(column):
        tnums[j][i] = nums[i][j]

# Step 2: Reverse each row (your logic, fixed safely)
i, j = 0, 0
while i < row and j < column:
    tnums[i][j], tnums[i][column - j - 1] = tnums[i][column - j - 1], tnums[i][j]
    j += 1
    if j == column // 2:  # ✅ Changed from `/` to `//` for integer comparison
        i += 1
        j = 0

print(tnums)
