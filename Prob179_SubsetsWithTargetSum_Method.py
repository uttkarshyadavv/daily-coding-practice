result = []
nums = [5, 9, 7]

def solve(index, subset, target):
    if sum(subset) == target:
        if index >= len(nums):
            result.append(subset.copy())
            return
    subset.append(nums[index])
    solve(index + 1, subset, target)
    subset.pop()
    solve(index + 1, subset, target)

# Example usage
solve(0, [], 14)
print(result)
