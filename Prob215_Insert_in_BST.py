def solution(node,val):
    if node is None:
        return TreeNode(val)
    if val<node.val:
        node.left=solution(node.left,val)
    elif val>node.right:
        node.right=solution(node.right,val)
    return node