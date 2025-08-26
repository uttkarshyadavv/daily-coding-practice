nums=[1,1,1,0,0,0,1,1,1,1,0]
k=2
#Sliding Window
def solution(nums,k):
    left=0
    right=0
    maxi=0
    zeros=0
    while right<len(nums):
        if nums[right]==0:
            zeros+=1
        if zeros>k:
            if nums[left]==0:
                zeros-=1
            left+=1
        if zeros<k:
            maxi=max(maxi,right-left+1)
    return maxi