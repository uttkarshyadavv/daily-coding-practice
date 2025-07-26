
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
n = len(nums)
maxi = float('-inf')

for i in range(n):
    sum = 0
    for j in range(i, n):
        sum += nums[j]
        if sum > maxi:
            maxi = sum

print(maxi)  # Output: 6
