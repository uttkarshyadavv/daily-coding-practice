#We have to use extra edges in the graphs
class DisjointSet:
    def __init__(self,n):
        self.parent =[i for i in range(n)]
        self.rank=[0]*n
    
    def find(self,u):
        if self.parent[u]!=u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]
    
    def union(self,u,v):
        pu=self.find(u)
        pv=self.find(v)
        if pu==pv:
            return False
        if self.rank[pu]<self.rank[pv]:
            self.parent[pu]=pv
        elif self.rank[pu]>self.rank[pv]:
            self.parent[pv]=pu
        else:
            self.parent[pv]=pu
            self.rank[pu]+=1
        return True


class Solution:
    def makeConnected(n,connections):
        ds=DisjointSet(n)
        extra_edges=0
        for u,v in connections:
            if not ds.union(u,v):
                extra_edges+=1
        components=0
        for i in range(n):
            if ds.find(i)==i:
                components+=1
            
        if extra_edges>= components-1:
            return components-1
        return -1


