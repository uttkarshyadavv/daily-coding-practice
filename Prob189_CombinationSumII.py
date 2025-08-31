def backtrack(index,total,subset,nums):
    nums.sort()
    n=len(nums)
    for i in range(index,n):
        if i>index and nums[i]==nums[i-1]:
            continue
        subset.append(nums[i])
        sum=total-nums[i]
        backtrack(i+1,sum,subset,nums) #Don't put index+1, Index is like fixed stuff whereas i is iterating for a particular index
