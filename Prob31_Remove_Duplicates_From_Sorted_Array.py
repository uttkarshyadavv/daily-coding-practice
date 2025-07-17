#do not use for loop as the number of element varies after removing duplicate
nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
n = len(nums)
i = 0
while i < len(nums) - 1:
    j = i + 1
    if nums[i] == nums[j]:
        nums.pop(j)  
        continue 
    i += 1
print(nums)
print(len(nums))
