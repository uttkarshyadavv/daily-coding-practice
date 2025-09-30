#Store: List or Matrix
#Graps: 0 index based graph vs 1 index based graph
#n= number of nodes and m= no. of edges
#We have to make a matrix of [n+1]*[n+1]
# Matrix storing method is good if we have m>>n bcz of space complexity issue
n=5
m=6
edges=[[1,2],[2,4],[3,4],[1,3],[3,5],[5,4]]
#1 based index graph
matrix=[[0 for _ in range(n+1)] for _ in range(n+1)]
for u,v in edges:
    matrix[u][v]=1
    matrix[v][u]=1
print(matrix)