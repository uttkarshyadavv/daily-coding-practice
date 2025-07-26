nums = [2, 4, 6, 7, 9, 11, 18, 19]
target = 6
n = len(nums)
def binaryrec(nums, low, high, target):
    if low > high:
        return -1
    mid = (low + high) // 2
    if nums[mid] > target:
        return binaryrec(nums, low, mid - 1, target)
    elif nums[mid] < target:
        return binaryrec(nums, mid + 1, high, target)
    else:
        return mid
result = binaryrec(nums, 0, n - 1, target)
print("Index of", target, ":", result)
