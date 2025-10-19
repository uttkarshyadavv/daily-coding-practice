#Kahn's Algorithm= TOPO SORT In BFS
#InDegree= What is coming Toward them
from collections import deque
def kahn(graph,V,edge):
    adj_list=[[] for _ in range(V)]
    indegrees=[0 for _ in range(V)]
    for u,v in edge:
        indegrees[v]+=1
        adj_list[u].append(v)
    queue=deque()
    result=[]
    for i in range(V):
        if indegrees[i]==0:
            queue.append(i)
    while len(queue)!=0:
        current_node=queue.popleft()
        result.append(current_node)
        for adjNode in adj_list[current_node]:
            indegrees[adjNode]-=1
            if indegrees[adjNode]==0:
                queue.append(adjNode)
    return result


    