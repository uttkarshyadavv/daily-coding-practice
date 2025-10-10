def Detect(V,edges):
    adj_list=[[] for _ in range(V)]
    for u,v in edges:
        adj_list[u].append(v)
        adj_list[v].append(u)
    visited=[0]*V
    def DFS(node,parent):
        if  visited[node]==0:
            visited[node]=1
        for i in adj_list[node]:
            if not visited[i]:
                DFS(i,node)
                return True
            elif i!= parent:
                return True
        return False
    for i in range(V):
        if not visited[i]:
            if DFS(i,-1):
                return True
    return False

    


