result = []
nums = [5, 9, 7]

def solve(index, subset):
    if index >= len(nums):
        result.append(subset.copy())
        return
    subset.append(nums[index])
    solve(index + 1, subset)
    subset.pop()
    solve(index + 1, subset)

# Example usage
solve(0, [])
print(result)
