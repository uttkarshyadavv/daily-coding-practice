def dfs(node,result,visited,adj):
    visited[node]=1
    result.append(node)
    for n in adj[node]:
        if visited[n]==0:
            dfs(n,result,visited,adj)

number_of_nodes=9
adjacency_list=[
    [],[2,8],[1,3,4],[2],[2,5],[4,6],[5,7],[6,8],[1,7,9],[8],
]
visited=[0]*(number_of_nodes+1)
result=[]
dfs(1,result,visited,adjacency_list)
print(result)

