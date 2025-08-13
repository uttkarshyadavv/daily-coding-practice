def floor(nums, target):
    low = 0
    high = len(nums) - 1
    ans = -1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] <= target:
            ans = nums[mid]
            low = mid + 1
        else:
            high = mid - 1
    return ans
