def solve(last,total,subset,nums,target,k,result):
    if total==target and len(subset)==k:
        result.append(subset.copy())
        return
    if total>target or len(subset)>k:
        return
    #whenever we have to open more and more roots in a recurrsion tree after choosing pick or not pick we use iteration
    for i in range(last,len(nums)):
        sum=total+i
        subset.append(i)
        solve(i+1,sum,subset,nums)
        subset.pop()




