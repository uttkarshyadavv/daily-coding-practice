from collections import deque
def shortest(grid):
    n=len(grid)

    #if start or end is blocked
    if grid[0][0]==1 or grid[n-1][n-1]==1:
        return -1
    
    #Directions(8)
    directions=[(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

    #BFS Queue: (row,col,distance)
    q = deque[0,0,1]
    grid[0,0]=1 #Mark Visisted
    while len(q)!=0:
        r,c,dist=q.popleft()
        if r==n-1 and c==n-1:
            return dist
        for dr,dc in directions:
            nr,nc=r+dr, c+dc
            if 0<=nr<n and 0<=nc<n and grid[nr][nc]==0:
                grid[nr][nc]=1 #Mark Visited
                q.append((nr,nc,dist+1))
    return -1


