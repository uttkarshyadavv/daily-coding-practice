#In this method you are gonna make a list of n+1 elements 
n=5
m=6
edges=[[1,2],[2,4],[3,4],[1,3],[3,5],[5,4]]
lst=[[] for _ in range(n+1)]
print(lst)
for u,v in edges:
    lst[u].append(v)
    lst[v].append(u)
print(lst)