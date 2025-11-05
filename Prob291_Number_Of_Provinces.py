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

        if pu!=pv:
            if self.rank[pu] < self.rank[pv]:
                self.parent[pu]=pv
            elif self.rank[pu] > self.rank[pv]:
                self.parent[pv]=pu
            else:
                self.parent[pv]=pu
                self.rank[pu]+=1
    
    def findCircleNum(isConnected,V):
        n=len(isConnected)
        ds=DisjointSet(n)

        for i in range(n):
            for j in range(i+1,n):
                if isConnected[i][j]==1:
                    ds.union(i,j)

        count=0
        for i in range(V):
            if ds.find(i)==i:
                count+=1

        return count
    

