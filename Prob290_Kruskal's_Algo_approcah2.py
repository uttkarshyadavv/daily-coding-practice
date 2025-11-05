class DisjointSet:
    def __init__(self,n):
        self.parent=[i for i in range(n)]
        self.rank=[0]*n

    def find(self,u):
        if self.parent[u]!=u:
            self.parent[u]= self.find(self.parent[u])
        return self.parent[u]
    
    def union(self,u,v):
        pu=self.find(u)
        pv=self.find(v)

        if pu!=pv:
            if self.rank[pu]< self.rank[pv]:
                self.rank[pu]=pv
            elif self.rank[pu] > self.rank[pv]:
                self.rank[pv]=pu
        else:
            self.parent[pv]=pu
            self.rank[pu]+=1
class Solution:            
    def kruskal(adj,V):
        edges=[]
        seen=set()

        #TC -> O(N+E)
        for u in range(V):
            for neighbour in adj[u]:
                v,w= neighbour
                if (min(u,v),max(u,v)) not in seen: #Tuple
                    seen.add((min(u,v),max(u,v)))
                    edges.append((w,u,v))
        
        #TC -> O(M logM)
        edges.sort()

        dsu=DisjointSet(V)
        mst_weight=0

        #TC -> O(M*4*alpha)
        for w,u,v in edges:
            if dsu.union(u,v):
                mst_weight+=w
        return mst_weight
        