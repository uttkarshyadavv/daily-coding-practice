from collections import deque
from copy import deepcopy
def flood(grid):
    rows=len(grid)
    cols=len(grid[0])
    grid_copy= deepcopy(grid)

    colour1=0
    queue= deque()
    for i in range(rows):
        for j in range(cols):
            if grid_copy[i][j]==2:
                queue.append((i,j))
            elif grid_copy[i][j]==1:
                colour1+=1
    while len(queue)!=0 and colour1>0:
        total_change=len(queue)
        for _ in range(total_change):
            i,j= queue.popleft()
            for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                new_i,new_j=i+dx, j+dy
                if new_i<0 or new_i== rows or new_j<0 or new_j==cols:
                    continue
                if grid_copy[new_i][new_j]==0 or \
                    grid_copy[new_i][new_j]==2:
                    continue
                colour1-=1
                grid_copy[new_i][new_j]=2
                queue.append((new_i,new_j))
    return grid_copy
