nums=[7,2,1,5,6,4,8]
n=len(nums)
profit = float("-inf")
for i in range(0,n):
    for j in range(i+1,n):
        if i==j or i>j:
            break
        if (nums[j]-nums[i])>profit:
            profit= nums[j]-nums[i]
print(profit)
