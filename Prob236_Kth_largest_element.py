arr=[3,2,1,5,6,4]
k=2
#we have to use minimum heap here
#we could directly use it form the libraries or write the whole code for that
#Priority Queue
import heapq
ans=[]
for i in range(k):
    heapq.heappush(ans,arr[i])
for i in range(k,len(arr)):
    if arr[i]>arr[0]:
        heapq.heappop(ans)
        heapq.heappush(ans,arr[i])
print(ans[0])
