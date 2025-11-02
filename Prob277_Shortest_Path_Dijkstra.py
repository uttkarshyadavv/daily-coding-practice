import heapq
import sys
def shortest(n,edge,m):
    adj_list=[[] for _ in range(n+1)]
    for u,v,wt in edge:
        adj_list[u].append([v,wt])
        adj_list[v].append([u,wt])
    distance=[sys.maxsize for _ in range(n+1)]
    distance[1]=0

    parent=[i for i in range(n+1)]
    priority_queue=[]
    priority_queue.append([0,1])
    while len(priority_queue)!=0:
        dist,node=heapq.heappop()
        for adjNode,wt in adj_list[node]:
            dist_trav=dist+wt
            if dist_trav<distance[adjNode]:
                distance[adjNode]=dist_trav
                heapq.heappush(priority_queue,[dist_trav,adjNode])
                parent[adjNode]=node
    if distance[n]==sys.maxsize:
        return [-1]
    node=n
    path=[]
    #TC -> O(V)
    while parent[node]!=node:
        path.append(node)
        node=parent[node]
    path.append(1)
    path.reverse()
    return path

    