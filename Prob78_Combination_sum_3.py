#make a list of k distinct numbers(No repetition) such that their sum comes out to be n
def combosum(k,target,subset,result,index,nums,total):
    if sum(subset)==target and k==len(subset):
        result.append(subset.copy())
        return result
    elif index>=len(nums) or len(subset)>k or total>target:
        return
    subset.append(nums[index])
    sum=total+nums[index]
    combosum(k,target,subset,result,index+1,nums,sum)
    subset.pop()
    sum=total
    combosum(k,target,subset,result,index+1,nums,sum)
nums=[1,2,3,4,5,6,7,8,9]
result=[]
combosum(3,9,[],result,0,nums,0)
print(result)

