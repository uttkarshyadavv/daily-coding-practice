nums=[4,7,1,1,2,-2,-7,17,15,-16]
n=len(nums)
stack=[]
for i in range(0,n):
    if nums[i]>0:
        stack.append(nums[i])
    else:
        while len(stack)!=0 and stack[-1]>0 and abs(nums[i])>stack[-1]:
            stack.pop()
        if abs(nums[i])==stack[-1] and len(stack)!=0:
            stack.pop()
        elif len(stack)==0 or stack[-1]<0:
            stack.append(nums[i])
print(stack)
        