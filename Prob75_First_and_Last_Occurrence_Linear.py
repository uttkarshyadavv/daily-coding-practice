#find the first and last occurance
nums=[5,7,7,8,8,8,8,8,10]
target=8
n=len(nums)
first,last=-1,-1
for i in range(0,n):
    if nums[i]==target:
        first=i
        break
    for j in range(i+1,n):
        if nums[j]==target:
            last=j
print(first,last)
