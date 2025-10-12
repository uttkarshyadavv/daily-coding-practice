#To get number of land which can't go out of boundary
#1's= land and 0's= Water
def dfs(r,c,visited,rows,column,mat):
    if r>=rows or r<0 or c>=column or c<0:
        return 
    if visited[r][c]==1:
        return
    if mat[r][c]==0:
        return
    visited[r][c]=1
    dfs(r-1,c,visited,rows,column,mat)
    dfs(r,c-1,visited,rows,column,mat)
    dfs(r,c+1,visited,rows,column,mat)
    dfs(r+1,c,visited,rows,column,mat)
def solve(mat):
    rows=len(mat)
    column=len(mat[0])
    visited=[[0]*column for _ in range(rows)]
    for r in range(rows):
        for c in range(column):
            if r==0 or c==0 or r==rows-1 or c== column-1:
                if mat[r][c]==1:
                    if visited[r][c]==0:
                        dfs(r,c,visited,rows,column,mat)
    count=0
    for r in range(rows):
        for c in range(column):
            if mat[r][c]==1 and visited[r][c]==0:
                count+=1
    return count

