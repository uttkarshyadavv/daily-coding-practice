def solve(self,col,board,ans,n):
    if col==n:
        ans.append(list(board))
        return
    #Putting Q at every column then after getting true from isSafe function, putting the Q and changing the row
    for row in range(n):
        if self.isSafe(row,col,board,n):
            board[row]=board[row][:col] + "Q" + board[row][col+1:]
            self.solve(col+1,board,ans,n)
            board[row]=board[row][:col]+"."+board[row][col+1:]
def isSafe(self,row,col,board,n):
    duprow=row
    dupcol=col
    while row>=0 and col>=0:
        if board[row][col]=="Q":
            return False
        row-=1
        col-=1
    col=dupcol
    row=duprow
    while col>=0:
        if board[row][col]=="Q":
            return False
        col-=1
    row=duprow
    col=dupcol
    while row<n and col>=0:
        if board[row][col]=="Q":
            return False
        row+=1
        col-=1
    return True
