def dfs(r,c,visited,rows,column,board):
    if r<0 or r>=rows or c<0 or c>=column:
        return
    if board[r][c]=="X":
        return
    if visited[r][c]==1:
        return
    visited[r][c]=1
    dfs(r-1,c,visited,rows,column,board)
    dfs(r,c-1,visited,rows,column,board)
    dfs(r,c+1,visited,rows,column,board)
    dfs(r+1,c,visited,rows,column,board)
def solve(board):
    rows=len(board)
    column=len(board[0])
    visited=[[0]*column for _ in range(rows)]
    #Upper Row
    r,c=0,0
    for c in range(column):
        if board[r][c]=="O":
                    if visited[r][c]==0:
                        dfs(r,c,visited,rows,column,board)
    #Last Rows
    r,c=rows-1,0
    for c in range(column):
        if board[r][c]=="O":
                    if visited[r][c]==0:
                        dfs(r,c,visited,rows,column,board)
    #First Column
    r,c=0,0
    for r in range(rows):
        if board[r][c]=="O":
                    if visited[r][c]==0:
                        dfs(r,c,visited,rows,column,board)
    #Last Column
    r,c=0,column-1
    for r in range(rows):
        if board[r][c]=="O":
                    if visited[r][c]==0:
                        dfs(r,c,visited,rows,column,board)
    for r in range(rows):
        for c in range(column):
            if r==0 or c==0 or r==rows-1 or c==column-1:
                if board[r][c]=="O":
                    if visited[r][c]==0:
                        dfs(r,c,visited,rows,column,board)
    for r in range(rows):
        for c in range(column):
            if board[r][c]=="O" and visited[r][c]==0:
                board[r][c]="X"
