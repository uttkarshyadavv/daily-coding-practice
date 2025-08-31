def solve(index,total,nums,result):
    if index>=len(nums):
        result.append(total)
        return result
    sum=total+nums[index]
    solve(index+1,sum,nums,result)
    sum=total
    solve(index+1,total,nums,result)
nums=[5,9,3]
result=[]
solve(0,0,nums,result)
print(result)
