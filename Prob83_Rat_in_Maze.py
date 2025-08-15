def findPathelper(
        i: int,
        j: int,
        a: list[list[int]],
        n: int,
        ans: list[str],
        move: str,
        vis: list[list[int]],        
):
    if i==n-1 and j==n-1:
        ans.append(move)
        return
    #downward
    if i+1<n and not vis[i+1][j] and a[i+1][j]==1:
        vis[i][j]=1
        findPathelper(i+1,j,a,n,ans,move+"D",vis)
        vis[i][j]=0

    #left
    if j-1>=0 and not vis[i][j-1] and a[i][j-1]==1:
        vis[i][j]=1
        findPathelper(i,j-1,a,n,ans,move+"L",vis)
        vis[i][j]=0
    
    #right
    if j+1<n and not vis[i][j+1] and a[i][j+1]==1:
        vis[i][j]=1
        findPathelper(i,j+1,a,n,ans,move+"R",vis)
        vis[i][j]=0
    
    #up
    if i-1>=0 and not vis[i-1][j] and a[i-1][j]==1:
        vis[i][j]=1
        findPathelper(i-1,j,a,n,move+"U",vis)
        vis[i][j]=0
def ratMaze(matrix: list[list[int]])->list[str]:
    n=len(matrix)
    ans=[]
    vis=[[0 for _ in range(n)] for _ in range(n)]
    if matrix[0][0] == 1:
        findPathelper(0, 0, matrix, n, ans, "", vis)
    return ans