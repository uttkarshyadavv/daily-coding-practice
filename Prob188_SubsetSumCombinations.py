def combinationsum(index,total,subset,target,nums,result):
    if total==target:
        result.append(subset.copy())
    elif total>target:
        return
    if index>=len(nums):
        return
    sum=total+nums[index]
    subset.append(nums[index])
    combinationsum(index,sum,subset)
    #when it is cooked then this part starts
    sum=total
    subset.pop()
    combinationsum(index+1,total,subset,target,nums,result)
def solve(candidate, target):
    result=[]
    solve(candidate,target)
    return result
