nums = [
    [7, 9, 2, 3],
    [20, 8, 0, 10],
    [29, 0, -10, 5],
    [4, 14, 6, 7]
]

def inf(nums, row, col):
    for i in range(len(nums)):
        nums[i][col] = float('inf')
    for j in range(len(nums[0])):
        nums[row][j] = float('inf')

r = len(nums)
c = len(nums[0])

# First pass: mark rows and columns to be zeroed
for i in range(r):
    for j in range(c):
        if nums[i][j] == 0:
            inf(nums, i, j)

# Second pass: convert marked cells to actual 0
for i in range(r):
    for j in range(c):
        if nums[i][j] == float('inf'):
            nums[i][j] = 0

print(nums)
