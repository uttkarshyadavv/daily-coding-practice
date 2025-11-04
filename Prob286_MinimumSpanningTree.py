#A tree with N nodes and N-1 edges and all the nodes should be reachable
#Prims Algo
import heapq
def prim(V,graph,adj):
    vis=[[0] for _ in range(n)]
    mst=[]
    sum=0
    vis=[0 for _ in range(V)]
    priority_queue=[]
    priority_queue.append([0,0,-1])
    while len(priority_queue)!=0:
        wt,node,parent= heapq.heappop(priority_queue)
        if vis[node]==0:
            vis[node]=1
            if parent!=-1:
                sum+=wt
                mst.append([parent,node])
            for adjNode,wtt in adj[node]:
                if vis[adjNode]==0:
                    heapq.heappush(priority_queue,[wtt,adjNode,node])
    return sum