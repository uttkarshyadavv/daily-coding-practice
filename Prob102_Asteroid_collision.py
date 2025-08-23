nums=[4,7,1,1,2,-3,-7,17,15,-18,-19]
i=0
while i<len(nums)-1:
    if nums[i]*nums[i+1]<0:
        if abs(nums[i])<abs(nums[i+1]):
            nums.pop(i)
            if i>0:
                i-=1
        elif abs(nums[i])==abs(nums[i+1]):
            nums.pop(i)
            nums.pop(i+1)
            if i>0:
                i-=1
        else:
            nums.pop(i+1)
    else:
        i+=1
print(nums)