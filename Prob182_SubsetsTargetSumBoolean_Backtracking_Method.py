result = []
nums = [5, 9, 7]
k = 14  # example target

def backtrack(index, total, subset):
    if total == k:
        result.append(subset.copy())
        return True
    elif total > k:
        return False
    if index >= len(nums):
        return False
    subset.append(nums[index])
    sum = total + nums[index]
    pick = backtrack(index + 1, total, subset)
    if pick == True:
        return True
    sum = total  # popped the last element
    not_pick = backtrack(index + 1, sum, subset)
    return not_pick

# Example usage
backtrack(0, 0, [])
print(result)
