#left -> right -> root
def postorder(node):
    if node==None:
        return
    postorder(node.left)
    postorder(node.right)
    print(node.val)