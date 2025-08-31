nums=[1,3,5,7]
n=len(nums)
def search(nums,target):
    low=0
    high=n-1
    lb=n
    while low<=high:
        mid= (low+high)//2
        if nums[mid]<=target:
            lb=mid
            low=mid+1
        elif nums[mid]>target:
            high=mid-1
    return lb