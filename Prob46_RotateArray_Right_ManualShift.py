nums=[1,2,3,4,5,6,7]
n=len(nums)
i=n-2
key=nums[n-1]
while i>-1:
    nums[i+1]=nums[i]
    i-=1
nums[0]=key
print(nums)
