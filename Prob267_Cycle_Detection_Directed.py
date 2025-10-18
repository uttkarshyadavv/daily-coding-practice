def dfs(node,visited,adj_list):
    visited[node]=1
    for adjNode in adj_list[node]:
        if visited[adjNode]==0:
            if dfs (adjNode,visited,adj_list):
                return True
        elif visited[adjNode]==1:
            return True
    return False
        
def cycle(graph,V,edges):
    adj_list=[[] for _ in range(V)]
    for u,v in edges:
        adj_list[u].append(v)
        adj_list[v].append(u)
    visited=[0]*len(graph)
    for i in range(0,V):
        if visited[i]==0:
            if dfs(i,visited,adj_list):
                return True
    return False