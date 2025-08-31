def subsetsum(nums, index, subset, result):
    if index >= len(nums):
        result.append(sum(subset))  # record sum of this subset
        return
    subset.append(nums[index])
    subsetsum(nums, index + 1, subset, result)
    subset.pop()
    subsetsum(nums, index + 1, subset, result)

nums = [1, 2, 3]
result = []
subsetsum(nums, 0, [], result)
print(result)
