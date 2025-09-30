n=5
m=6
edges=[[1,2],[2,4],[3,4],[1,3],[3,5],[5,4]]
#1 based index graph
matrix=[[0 for _ in range(n+1)] for _ in range(n+1)]
for u,v in edges:
    matrix[u][v]=1
print(matrix)

n=5
m=6
edges=[[1,2],[2,4],[3,4],[1,3],[3,5],[5,4]]
lst=[[] for _ in range(n+1)]
print(lst)
for u,v in edges:
    lst[u].append(v)
print(lst)