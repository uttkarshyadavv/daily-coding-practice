#0== Sea water
#1== Land
def dfs(mat,r,c,visited,rows,column):
    if r<0 or r>=rows or c<0 or c>=column:
        return
    if mat[r][c]==0 or visited[r][c]==1:
        return
    visited[r][c]=1
    dfs(mat,r+1,c,visited,rows,column)
    dfs(mat,r-1,c,visited,rows,column)
    dfs(mat,r,c+1,visited,rows,column)
    dfs(mat,r,c-1,visited,rows,column)
def island(mat):
    rows=len(mat)
    column=len(mat[0])
    visited=[[0]*column for _ in range(rows)]
    count=0
    for r in range(rows):
        for c in range(column):
            if mat[r][c]==1 and visited[r][c]==0:
                dfs(mat,r,c,visited,rows,column)
                count+=1
    return count
    