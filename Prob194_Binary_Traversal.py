#Depth First 
#preorder
def preorder(node):
    if node==None:
        return
    print(node.val, end=" ")
    preorder(node.left)
    preorder(node.right)