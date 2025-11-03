import heapq
def func(start,end,mod,arr):
    dist= [float("inf")]*mod
    dist[start]=0
    pq=[(0,start)]
    while pq:
        steps,val= heapq.heappop(pq)
        if val==end:
            return steps
        for num in arr:
            nxt=(val*num)%mod
            if steps+1< dist[nxt]:
                dist[nxt]=steps+1
                heapq.heappush(pq,(steps+1,nxt))
    return -1