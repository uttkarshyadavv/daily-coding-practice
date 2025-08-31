result = []
nums = [5, 9, 7]
k = 14  # example target

def backtrack(index, total, subset):
    if total == k:
        result.append(subset.copy())
        return
    elif total > k:
        return
    if index >= len(nums):
        return
    subset.append(nums[index])
    sum = total + nums[index]
    backtrack(index + 1, total, subset)
    e = subset.pop()
    sum -= e
    backtrack(index + 1, sum, subset)

# Example usage
backtrack(0, 0, [])
print(result)
