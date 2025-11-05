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

    def kruskal(n,edges):
        ds= DisjointSet(n)
        mst=[]
        edges.sort(key=lambda x:x[2])  #Sort By weight
        for u,v,w in edges:
            if ds.find(u) != ds.find(v):
                ds.union(u,v)
                mst.append((u,v,w))
        return mst
    
    