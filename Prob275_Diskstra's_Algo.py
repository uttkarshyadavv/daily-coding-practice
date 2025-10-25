import heapq
#Here we have three ways to implement 1) Queue 2) Priority Queue 3) Set
def diskstra(src,edges,V):
    adj_list=[[] for _ in range(V)]
    for u,v,d in edges:
        adj_list[u].append([v,d])
    distance=[float("inf") for _ in range(V)]
    distance[src]=0
    priority_queue=[[0,src]]
    while len(priority_queue)!=0:
        curr_dist,node=heapq.heappop(priority_queue)
        if curr_dist< distance(node):
            continue
        for adjNode, weight in adj_list[node]:
            dist_travel=curr_dist+weight
            if dist_travel< distance[adjNode]:
                distance[adjNode]= dist_travel
                priority_queue.append([dist_travel,adjNode])
    return distance


