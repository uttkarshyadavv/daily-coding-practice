nums=[3,3,3,1,2,1,1,2,3,3,4]
max_length=0
n=len(nums)
for i in range(0,n):
    my_set=set()
    for j in range(i,n):
        my_set.add(nums[j])
        if len(my_set)>2:
            break
        max_length=max(max_length,j-i+1)
print(max_length)
    