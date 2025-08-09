nums=[1,1,1,2,3,3,5,6,7,7,7,9,12,12,13]
target=8
n=len(nums)
def upperbound(nums,target):
    low=0
    high=n-1
    ub=n
    while low<high:
        mid=(low+high)//2
        if nums[mid]<=target:
            low=mid+1
        elif nums[mid]>target:
            ub=mid
            high=mid-1
    return ub
