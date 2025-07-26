nums = [-1, 0, 1, 2, -1, -4]
target = 0
result = set()
n = len(nums)
for i in range(n):
    my_set = set()
    for j in range(i + 1, n):
        third = -(nums[i] + nums[j])
        if third in my_set:
            temp = [nums[i], nums[j], third]
            temp.sort()
            result.add(tuple(temp))
        my_set.add(nums[j])
print([list(ans) for ans in result])
