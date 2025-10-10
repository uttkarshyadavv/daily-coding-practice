from collections import deque
def Detect_Cycle(V,edges):
    adj_list=[[] for _ in range(V)]
    for u,v in edges:
        adj_list[u].append(v)
        adj_list[v].append(u)
    visited=[0]*V
    for i in range(0,V):
        if visited[i]==1:
            continue
        queue=deque()
        queue.append((i,-1))
        visited[0]=1
        while len(queue)!=0:
            node,parent=queue.popleft()
            for adjNode in adj_list:
                if visited[adjNode]==0:
                    visited[adjNode]=1
                    queue.append(adjNode,node)
                else:
                    if adjNode != parent:
                        return True
        return False


