nums=[1,2,3]
y=[]
i=0
while i<len(nums):
    if nums[i]==0:
        x=nums.pop(i)
        y.insert(i,x)
    i+=1
print(y)
print(nums)
result=list(nums)+list(y)
print(result)
