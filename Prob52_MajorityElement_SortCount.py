nums = [2,1,1,1,1,2,2]
count = 0
n = len(nums)
i = 0
nums.sort()

while i < n:
    value = nums[i]
    count = 1
    i += 1
    while i < n and nums[i] == value:
        count += 1
        i += 1
    if count > n/2:
        print(value)
        break
