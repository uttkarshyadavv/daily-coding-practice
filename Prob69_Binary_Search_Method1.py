def binary_search(nums, target):
    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] > target:
            high = mid - 1
        elif nums[mid] < target:
            low = mid + 1
        else:
            return mid  # Target found

    return -1  # Target not found
nums = [2, 4, 6, 7, 9, 11, 18, 19]
target = 6
result = binary_search(nums, target)
print("Index of", target, ":", result)
