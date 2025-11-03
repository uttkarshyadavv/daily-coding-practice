from heapq import heappush,heappop

def minimumEffortPath(heights):
    n,m=len(heights), len(heights[0])
    directions=[(1,0),(0,1),(-1,0),(0,-1)]
    efforts=[[float("inf")]*m for _ in range(n)]
    efforts[0][0]=0
    pq=[(0,0,0)]
    while pq:
        eff,r,c=heappop(pq)
        if r==n-1 and c==n-1:
            return eff
        for dr,dc in directions:
            nr,nc=r+dr,c+dc
            if 0<=nr<n and 0<=nc<n:
                new_eff=max(eff,abs(heights[nr][nc] - heights[r][c]))
                if new_eff<efforts[nr][nc]:
                    efforts[nr][nc]= new_eff
                    heappush(pq,(new_eff,nr,nc))
    return 0