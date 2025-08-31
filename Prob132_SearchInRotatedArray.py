nums=[9,10,11,15,20]
def find(nums,target,k):
    n=len(nums)
    nums[:]=nums[n-k:]+nums[:n-k]
    print(nums)
    high=n-1
    low=0
    while low<=high:
        mid=(low+high)//2
        if nums[mid]==target:
            return mid
        if k-1<=mid:
            if target>nums[high]:
                high=mid-1
            else:
                low=mid+1
        elif k-1>nums[mid]:
            if target<=nums[high]:
                low=mid+1
            elif target>nums[high]:
                high=mid-1
    return -1

i=find(nums,11,4)
print(i)