#union(u,v)
# 1) Find ultimate parent of u and v, pu and pv
# 2) Find rank of pu and pv
# 3) Connect Smaller rank with larger rank 
# rank is not height
class DisjointSet:
    def __init__(self,n):
        self.parent= [i for i in range(0,n+1)]
        self.rank= [0]*(n+1)

    def find(self,x):
        if x==self.parent[x]:
            return x
        
        self.parent[x]=self.find(self.parent[x])
        return self.parent[x]
    
    def union(self,u,v):
        pu= self.find(u)
        pv= self.find(v)

        if pu==pv:
            return
        
        if self.rank[pu]< self.rank[pv]:  #pu -> pv
            self.parent[pu]=pv
        elif self.rank[pu]> self.rank[pv]:
            self.parent[pv]= pu
        else:
            self.parent[pv]= pu
            self.rank[pu]+=1