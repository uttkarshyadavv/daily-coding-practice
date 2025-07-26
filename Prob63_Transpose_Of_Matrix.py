nums = [
    [5, 8, 9],
    [10, 7, 6]
]
r = len(nums)
c = len(nums[0])
tnums = [[0] * r for _ in range(c)]
print("Before Transpose:", tnums)
for i in range(r):
    for j in range(c):
        tnums[j][i] = nums[i][j]
print("After Transpose:", tnums)
