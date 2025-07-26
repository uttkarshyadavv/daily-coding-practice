
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
n = len(nums)
total = 0
maxi = float('-inf')

for i in range(n):
    total += nums[i]
    if total < 0:
        total = 0
    elif total > maxi:
        maxi = total

print(maxi)
