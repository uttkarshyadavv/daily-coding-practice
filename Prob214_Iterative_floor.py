floor= -1
def solution(node,val):
    if node is None:
        return None
    if node.val==val:
        return node.val
    elif node.val>val:
        node=node.left
    else:
        floor=node.val
        node=node.right
    return floor