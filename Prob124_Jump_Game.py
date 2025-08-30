nums=[2,3,1,1,4]
n=len(nums)
max_reach=0
for i in range(0,n):
    if i>max_reach:
        print(False)
        break
    max_reach=max(max_reach,i+nums[i])
    if max_reach>=n-1:
        print(True)
        break