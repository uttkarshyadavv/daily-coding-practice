from copy import deepcopy
def dfs (i,j,new_color,initial_color,vis,row,column):
    if i<0 or j<0 or i>=row or j>=column:
        return 
    if vis[i][j]!=initial_color:
        return
    if vis[i][j]==new_color:
        return
    vis[i][j]=new_color
    dfs (i+1,j,new_color,initial_color,vis,row,column)
    dfs (i,j-1,new_color,initial_color,vis,row,column)
    dfs (i-1,j,new_color,initial_color,vis,row,column)
    dfs (i,j+1,new_color,initial_color,vis,row,column)
def flood(sr,sc,mat,color):
    initial_color=mat[sr][sc]
    if mat[sr][sc]==color:
        return mat
    vis= deepcopy(mat)
    row=len(vis)
    column=len(vis[0])
    dfs (sr,sc,color,initial_color,vis,row,column)




       
