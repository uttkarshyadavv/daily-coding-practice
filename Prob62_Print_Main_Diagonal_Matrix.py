nums = [
    [5, 10, 8],
    [7, 6, 3],
    [2, 1, 9]
]
row = len(nums)
column = len(nums[0])
for i in range(row):
    for j in range(column):
        if i == j:
            print(nums[i][j])
