import random
class Solution:
    def findKthlargest(self,nums,k):
        left,right=0,len(nums)-1
        while True:
            pivotIndex= self.randomIndex(left,right)
            pivotIndex= self.partitionandreturnIndex(nums, pivotIndex,left,right)
            if pivotIndex ==k-1:
                return nums[pivotIndex]
            elif pivotIndex>k-1:
                right= pivotIndex-1
            else:
                left= pivotIndex+1
    def randomIndex(self,left,right):
        return random.randint(left,right)
    def partitionandreturnIndex(self,nums, pivotIndex,left,right):
        pivot=nums[pivotIndex]
        nums[left],nums[pivotIndex]=nums[pivotIndex],nums[left]
        ind=left+1
        for i in range(left+1, right+1):
            if nums[i]>pivot:
                nums[ind],nums[i]=nums[i],nums[ind]
                ind+=1
        #Place the pivot at the corrected index
        nums[left], nums[ind-1]= nums[ind-1], nums[left]
        return ind-1
    