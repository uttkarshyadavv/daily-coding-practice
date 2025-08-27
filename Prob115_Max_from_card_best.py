nums=[1,2,3,4,5,6,1]
n=len(nums)
k=3
if n==k:
    print(sum(nums))
left_sum,right_sum=0,0
for i in range(0,k):
    left_sum+=nums[i]
maxi=left_sum
right_index=n-1
for i in range(k-1,-1,-1):
    left_sum-=nums[i]
    right_sum+=nums[right_index]
    right_index-=1
    maxi=max(maxi,left_sum+right_sum)
print(maxi)

