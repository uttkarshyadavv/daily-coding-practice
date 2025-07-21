nums = [1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1]
n = len(nums)
count = 0
max1 = 0
i = 0
while i < n:
    if nums[i] == 1:
        count += 1
        i += 1
    elif nums[i] != 1:
        if count > max1:
            max1 = count
        count = 0
        i += 1
if count > max1:
    max1 = count
print(max1)
