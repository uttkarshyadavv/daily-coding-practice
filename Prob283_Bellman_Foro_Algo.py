#Negative weight
#1)Relax all the edges by N-1 times sequentially
#2) if dist[u]+w< dist[v]: --> dist[v]=dist[u]+w
def bellmanFord(V,edges,src):
    dist=[float("inf") for _ in range(V)]
    dist[src]=0
    #TC -> O(V*E)
    for _ in range(V-1):
        for u,v,w in edges:
            if dist[u]!=float("inf"):
                if dist[u]+w < dist[v]:
                    dist[v]= dist[u] +w
    
    for u,v,w in edges: #Negative Cycle Detection
            if dist[u]!=float("inf"):
                if dist[u]+w < dist[v]:
                     return [-1]
    return dist