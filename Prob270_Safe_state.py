from collections import deque
def safestate(graph,V,edge):
    adj_list=[[] for _ in range(V)]
    indegree=[0*V]
    for node in range(V):
        for adjnode in graph[node]:
            adj_list[adjnode].append(node)
    for node in range(len(adj_list)):
        for adjNode in adj_list[node]:
            indegree[adjNode]+=1
    queue=deque()
    result=[]
    for i in range(V):
        if indegree[i] == 0:
            queue.append(i)
    #It clears the nodes which are not having circular dependency
    while len(queue)!=0:
        node=queue.popleft()
        result.append(node)
        for adjNode in adj_list[node]:
            indegree-=1
            if indegree[adjNode]==0:
                queue.append(adjNode)                                        
    return sorted(result)

    
