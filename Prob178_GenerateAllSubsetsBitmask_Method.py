nums = [1, 2, 3]  # example
n = len(nums)

total_subsets = 1 << n  # 2^n → 8 subsets for n=3
result = [[]]

for num in range(0, total_subsets):
    lst = []
    for i in range(0, n):
        if num & (1 << i) != 0:
            lst.append(nums[i])
    result.append(lst)

print(result)
