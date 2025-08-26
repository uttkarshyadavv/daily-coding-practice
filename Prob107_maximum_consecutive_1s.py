nums=[1,1,1,0,0,0,1,1,1,1,0]
k=2
def solution(left,right,k):
    left=0
    right=0
    j=0
    maxi=0
    while right<len(nums):
        if nums[right]==1:  
            right+=1
            maxi=max(maxi,right-left)
        elif nums[right]==0 and j<k: 
            j+=1
            right+=1
            maxi=max(maxi,right-left)
        else:
            if nums[left]==0:
                j-=1
            left+=1
    return maxi

u=solution(0,0,2)
print(u)  