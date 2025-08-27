nums = [1, 2, 3, 4, 5, 6, 1]
k=3
def solution(nums,k):
    left_sum=nums[:k]
    right_sum=nums[-k:]
    maxi=max(sum(left_sum),sum(right_sum))
    left=0
    right=len(nums)-1
    mid_sum=[]
    mid_sum.append(nums[left])
    mid_sum.append(nums[right])
    while len(mid_sum)<k:
        if left<k-1:
            left+=1
            mid_sum.append(nums[left])
            maxi=max(maxi,sum(mid_sum))
        elif right>=len(nums)-k+1:
            right-=1
            mid_sum.append(nums[right])
            maxi=max(maxi,sum(mid_sum))
    return maxi
u=solution(nums,k)
print(u)
    