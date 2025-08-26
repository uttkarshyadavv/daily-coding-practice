nums=[3,3,3,1,2,1,1,2,3,3,4]
#Using Dictionary
def solution(nums):
    left=0
    right=0
    freq={}
    maxi=0
    while right<len(nums):
        if nums[right] not in freq:
            freq[nums[right]]=1
        else:
            freq[nums[right]]+=1
        if len(freq)>2:
            while len(freq)>2:
                left+=1
                freq[nums[left]]-=1
                if freq [nums[left]]==0:
                    del freq[nums[left]]
        maxi=max(maxi,right-left+1)
        right+=1
    return maxi
