def dfs(mat,r,c,base_r,base_c,shape,visited,rows,column):
    visited[r][c]=1
    shape.append((r-base_r,c-base_c,)) #Tuple Append
    for x,y in [(-1,0),(0,-1),(1,0),(0,1)]:
        new_i,new_j=r+x, c+y
        if new_i<0 or new_j<0 or new_i>=rows or new_j>=column:
            continue
        if mat[new_i][new_j]==0:
            continue
        if visited[new_i][new_j]==1:
            continue
        dfs(mat,new_i,new_j,base_r,base_c,shape,visited,rows,column)
def disisland(mat):
    rows=len(mat)
    column=len(mat[0])
    visited=[[0]*column for _ in range(rows)]
    unique_islands=set()
    #Right--> Down --> Left --> Up
    for r in range(rows):
        for c in range(column):
            if mat[r][c]==1 and visited[r][c]==0:
                shape=[]
                dfs(mat,r,c,r,c,shape,visited,rows,column)
                unique_islands.add(tuple(shape))
    return len(unique_islands)