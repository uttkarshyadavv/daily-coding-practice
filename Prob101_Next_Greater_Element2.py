nums=[2,10,12,1,11]
n=len(nums)
ans=[-1]*n
stack=[]

# Process circularly by going through the array twice
for i in range(2*n-1, -1, -1):
    current_index = i % n
    while stack and stack[-1] <= nums[current_index]:
        stack.pop()
    if stack:
        ans[current_index] = stack[-1]
    stack.append(nums[current_index])
print(ans)