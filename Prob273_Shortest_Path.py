#Use BFS 
from collections import deque
def shortest(adj,src):
    n=len(adj)
    distance=[-1 for _ in range(n)]
    queue=deque()
    queue.append([src,0])
    distance[src]=0
    while len(queue)!=0:
        node,dist_trav=queue.popleft()
        for adjNode in adj[node]:
            if distance[adjNode]==-1:
                distance[node]= dist_trav+1
                queue.append([adjNode,dist_trav+1])
    return distance


    