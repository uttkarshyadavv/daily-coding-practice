#For matrix approach
n=5
m=6
edges=[[1,2,3],[2,4,3],[3,4,6],[1,3,2],[3,5,8],[5,4,3]]
#1 based index graph
matrix=[[0 for _ in range(n+1)] for _ in range(n+1)]
for u,v,w in edges:
    matrix[u][v]=w
    matrix[v][u]=w
print(matrix)

#For List approach
n=5
m=6
edges=[[1,2,3],[2,4,3],[3,4,6],[1,3,2],[3,5,8],[5,4,3]]
lst=[[] for _ in range(n+1)]
print(lst)
for u,v,w in edges:
    lst[u].append([v,w])
    lst[v].append([u,w])
print(lst)

