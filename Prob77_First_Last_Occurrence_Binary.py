#find the first and last occurance
#nums[i]>=target (lb) and nums[i]>target (ub)
def lb(nums,target):
    n=len(nums)
    low=0
    high=n-1
    lb=-1
    while low<=high:
        mid=(low+high)//2
        if nums[mid]<target:
            low=mid+1
        elif nums[mid]>=target:
            lb=mid
            high=mid-1       
    return lb
def ub(nums,target):
    n=len(nums)
    low=0
    high=n-1
    ub=-1
    while low<=high:
        mid=(low+high)//2
        if nums[mid]<=target:
            low=mid+1
        elif nums[mid]>target:
            ub=mid
            high=mid-1        
    return ub
lower=lb([5,7,7,8,8,8,8,8,10],8)
ipper=ub([5,7,7,8,8,8,8,8,10],8)
print(lower,ipper-1)
