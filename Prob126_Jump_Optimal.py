nums=[2,3,1,4,1,1,1,2]
jump=0
left=0
right=0
n=len(nums)
while right<n-1:
    farthest=0
    for i in range(left,right+1):
        farthest=max(farthest,i+nums[i])
    left=right+1
    right=farthest
    jump+=1
print(jump)
