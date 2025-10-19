def dfs(current_node,adj_list,vis,path_vis,is_safe):
    vis[current_node]=1
    path_vis[current_node]=1
    for adjNode in adj_list[current_node]:
        if vis[adjNode]==0:
            ans= dfs(adjNode,adj_list,vis,path_vis,is_safe)
            if ans==False:
                return False
        elif path_vis[adjNode]==1: #If I find a neighbor (adjNode) that’s already in the current recursion path, I’ve found a cycle.
                return False
    is_safe[current_node]=1
    path_vis[current_node]=0
    return True
def eventalSafeNodes(graph):
    V=len(graph)
    vis=[0 for _ in range(V)]
    path_vis= [0 for _ in range(V)]
    is_safe= [0 for _ in range(V)]

    for i in range(V):
        if vis[i]==0:
            dfs(i,graph,vis,path_vis,is_safe)
    result=[]
    for i in range(V):
        if is_safe[i]==1:
            result.append(i)
    return result



    
