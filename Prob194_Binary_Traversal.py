#Depth First 
#preorder
#root -> left -> right
def preorder(node):
    if node==None:
        return
    print(node.val, end=" ")
    preorder(node.left)
    preorder(node.right)