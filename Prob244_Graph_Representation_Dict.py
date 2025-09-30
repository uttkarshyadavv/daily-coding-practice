#dct={1:[],2:[],3:[],4:[],5:[]}
n=5
m=6
edges=[[1,2],[2,4],[3,4],[1,3],[3,5],[5,4]]
my_dict={}
for i in range(1,n+1):
    my_dict[i]=[]
print(my_dict)
for u,v in edges:
    my_dict[u].append(v)
    my_dict[v].append(u)
print(my_dict)