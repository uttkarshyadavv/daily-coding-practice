#Topological Sort (DFS)
#Ordering of nodes in such a way that if there is an edge between u and v, u should appear before v in that ordering
#Graph Should be Directed Acyclic Graph (DAG)
def dfs(V,edges,adj_list,stack,visited, current_node):
    visited[current_node]=1
    for adjNode in adj_list[current_node]:
        if visited[adjNode]==0:
            dfs(V,edges,adj_list,stack,visited, adjNode)
    stack.append(current_node)

def toposort(V,edges):
    adj_list=[[]for _ in range(V)]
    for u,v in edges:
        adj_list[u].append(v)
        adj_list[v].append(u)
    
    stack=[]
    visited= [0 for _ in range(V)]
    for i in range(0,V):
        dfs(V,edges,adj_list,stack,visited)
    return stack[::-1]