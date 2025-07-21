nums = [11, 24, 3, 46, 5, 6, 78]
n = len(nums)
largest = nums[0]
for i in range(0, n):
    for j in range(i + 1, n):
        if nums[i] > nums[j]:
            if nums[i] > largest:
                largest = nums[i]
        else:
            if nums[j] > largest:
                largest = nums[j]
print("Largest:", largest)
if nums[0] != largest:
    s_largest = nums[0]
else:
    s_largest = nums[1]

for k in range(0, n):
    if nums[k] != largest and nums[k] > s_largest:
        s_largest = nums[k]
print("Second Largest:", s_largest)
