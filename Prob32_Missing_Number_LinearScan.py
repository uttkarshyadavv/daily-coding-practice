nums=[3,0,1]
y=[]
for i in range(0,len(nums)):
    y.append(i)
y.append(len(nums))
i,j=0,0
m,n=len(nums),len(y)
while i<m and j<n:
    if nums[i]!=y[j]:
        i+=1
        continue
    else:
        i=0
        j+=1
print(j)
