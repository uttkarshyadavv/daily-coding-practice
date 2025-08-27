nums=[1,2,3,4,4,6,1]
k=3
def solution(nums,k):
    left=0
    result1=[]
    result2=[]
    result3=[]
    result4=[]
    right=len(nums)-1
    i=0
    maxi=0
    for left in range(0,k):
        result1.append(nums[left])
        maxi=max(maxi,sum(result1))
    result1.pop()
    for right in range(len(nums)-1,k,-1):
        result2.append(nums[right])
        maxi=max(maxi,sum(result2))
    result2.pop()
    result3.append(result1[0])
    result3.append(result2[0])
    result1.pop(0)
    result2.pop(0)
    result4=result1+result2
    for i in range(0,len(result1)+len(result2)):
        result3.append(result4[i])
        maxi=max(maxi,sum(result4))
        result3.pop()
    return maxi
u=solution(nums,k)
print(u)






