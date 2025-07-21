nums = [2,0,2,1,1,0]
i=0
j=i+1
min_value=i
n=len(nums)
for i in range(0,n-1):
    for j in range(i+1,n):
        if nums[j]<nums[i]:
            min_value=j
            nums[i],nums[j]=nums[j],nums[i]
print(nums)
