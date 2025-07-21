nums = [3,1,-2,-5,2,-4]
positive=[]
negative=[]
result=[]
i=0
n=len(nums)
while i<n:
    if nums[i]>0:
        positive.append(nums[i])
        i+=1
    else:
        negative.append(nums[i])
        i+=1
print(positive)
print(negative)
i,j=0,0
m,p=len(positive),len(negative)
while i<m and j<p:
    result.append(positive[i])
    result.append(negative[j])
    i+=1
    j+=1
print(result)
