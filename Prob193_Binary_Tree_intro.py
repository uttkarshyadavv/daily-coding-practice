class Nodes:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
drinks= Nodes("drinks")
hot=Nodes("hot")
cold=Nodes("cold")
tea=Nodes("tea")
coffee=Nodes("coffee")
cola=Nodes("cola")
fanta=Nodes("fanta")

hot.left=tea
hot.right=coffee

cold.left=cola
cold.right=fanta

drinks.left=hot
drinks.right=cold

print(drinks.left.val)
print(hot)
