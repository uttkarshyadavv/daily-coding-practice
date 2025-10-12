#Nearest Zero
from collections import deque
from copy import deepcopy
def Near(mat,r,c):
    image=deepcopy(mat)
    rows=len(image)
    column=len(image[0])
    visited=[[0]*column for _ in range (rows)]
    distance= [[0]*column for _ in range (rows)]
    queue=deque()
    for i in range(rows):
        for j in range(column):
            if mat[i][j]==0:
                queue.append([i,j,0])
                visited[i][j]=1
    while len(queue)!=0:
        r,c,d=queue.popleft()
        distance[r][c]=d
        for x,y in [(-1,0),(0,-1),(1,0),(0,1)]:
            new_i,new_j= i+x, j+y
            if visited[new_i][new_j]==1:
                continue
            if new_i<0 or new_i>rows or new_j<0 or new_j>column:
                continue
            queue.append([new_i,new_j,d+1])
            visited[new_i][new_j]=1
    return distance
