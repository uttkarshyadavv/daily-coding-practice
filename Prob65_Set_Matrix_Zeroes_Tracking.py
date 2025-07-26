nums = [
    [7, 10, 29, 3],
    [1, 20, 0, 4],
    [9, 0, 6, 11],
    [4, 27, 14, 7]
]
row = len(nums)
column = len(nums[0])
row_tracker = [0] * row
column_tracker = [0] * column
# First pass: track rows and columns with 0s
for i in range(row):
    for j in range(column):
        if nums[i][j] == 0:
            row_tracker[i] = -1
            column_tracker[j] = -1
print("Row Tracker:", row_tracker)
print("Column Tracker:", column_tracker)
# Second pass: zero out marked rows and columns
for i in range(row):
    for j in range(column):
        if row_tracker[i] == -1 or column_tracker[j] == -1:
            nums[i][j] = 0

print(nums)
