nums = [5, 9, 7]
k = 14  # example target

def backtrack(index, total):
    if total == k:
        return 1
    elif total > k:
        return 0
    elif index >= len(nums):
        return 0
    sum = total + nums[index]
    pick = backtrack(index + 1, sum)
    sum = total
    not_pick = backtrack(index + 1, sum)
    return pick + not_pick

# Example usage
print(backtrack(0, 0))  # count of valid subsets
