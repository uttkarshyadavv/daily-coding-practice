nums=[2,3,1,4,1,1,1,2]
def Solution(index,jump):
    n=len(nums)
    if index>=nums[n-1]:
        return jump
    min_jump=float("inf")
    for i in range(1,nums[i]+1):
        min_jump=min(min_jump,Solution(index+i,jump+1))
    return min_jump



