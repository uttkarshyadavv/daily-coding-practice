def ceil(nums, target):
    low, high = 0, len(nums) - 1
    ans = None  # Use None to indicate no ceil found yet
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] >= target:
            ans = nums[mid]
            high = mid - 1
        else:
            low = mid + 1
    return ans if ans is not None else -1
