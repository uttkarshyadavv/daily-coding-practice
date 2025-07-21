nums=[1,2,3,4]
target=5
n=len(nums)
i=0
j=1
while i<n-1 and j<n:
    if nums [i]+nums[j]==target:
        print(i,j)
        break
    elif nums [i]+nums[j]!=target and j<n-1:
        j+=1
    else:
        i+=1
