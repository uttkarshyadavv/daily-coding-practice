#It's Bad because of time complexity O(V^2) whereas for the other method it's O(V)
import sys
def diskstra(V,edges,src):
    adj_list=[[] for _ in range(V)]
    for u,v,d in edges:
        adj_list[u].append((v,d))
    distance= [sys.maxsize for _ in range(V)]
    distance[src]=0
    my_set=set()
    my_set.add((0,src))
    while len(my_set)!=0: #O(V)
        dist,node=min(my_set) #O(V)
        my_set.discard((dist,node))
        for adjNode, weight in adj_list[node]:
            dist_trav= dist+weight
            if dist_trav < distance[adjNode]:
                if distance[adjNode]!= sys.maxsize:
                    my_set.discard((distance[adjNode],adjNode)) #Tuple
                distance[adjNode]=dist_trav
                my_set.add((dist_trav,adjNode)) #Tuple
    return distance
        



