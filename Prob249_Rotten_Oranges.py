#0= Nothing is their 
#1= Fresh Orange is their
#2= Rotten Orange is their
# Up=(-1,0) left=(0,-1) down=(1,0) right=(0,1)
from collections import deque
from copy import deepcopy
def orangesRotting(grid):
    rows=len(grid)
    cols=len(grid[0])
    grid_copy= deepcopy(grid)

    fresh_Orange=0
    queue= deque()
    for i in range(rows):
        for j in range(cols):
            if grid_copy[i][j]==2:
                queue.append((i,j))
            elif grid_copy[i][j]==1:
                fresh_Orange+=1
    minutes=0
    while len(queue)!=0 and fresh_Orange>0:
        minutes+=1
        total_rotten=len(queue)
        for _ in range(total_rotten):
            i,j= queue.popleft()
            for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                new_i,new_j=i+dx, j+dy
                if new_i<0 or new_i== rows or new_j<0 or new_j==cols:
                    continue
                if grid_copy[new_i][new_j]==0 or \
                    grid_copy[new_i][new_j]==2:
                    continue
                fresh_Orange-=1
                grid_copy[new_i][new_j]==2
                queue.append((new_i,new_j))
    if fresh_Orange>0:
        return -1
    return minutes