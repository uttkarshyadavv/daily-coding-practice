arr=[900,940,950,1100,1500,1800]
dep=[910,1200,1120,1130,1900,2000]
dep.sort()
print(arr,dep)
def solution(arr,dep):
    i=1
    j=0
    ans=1
    count=1
    while i<len(arr)-1 and j<len(arr)-1:
        if arr[i]<=dep[j]:
            count+=1
            i+=1
        else:
            count-=1
            j+=1
        ans(max(ans,count))
    return ans
