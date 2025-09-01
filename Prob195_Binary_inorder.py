#inorder(left -> root -> right)
def inorder(node):
    if node==None:
        return
    inorder(node.left)
    print(node.val)
    inorder(node.right)