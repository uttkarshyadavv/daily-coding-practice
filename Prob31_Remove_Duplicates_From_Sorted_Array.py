nums = [0, 1, 0, 1, 2, 2, 4, 3, 4, 4]
for i in range(len(nums)):
    j = i + 1
    while j < len(nums):
        if nums[i] == nums[j]:
            nums.pop(j)
        else:
            j += 1 
print(nums)
