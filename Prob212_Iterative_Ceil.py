ceil=-1
def solution(node,input,ceil):
    while node is not None:
        if node.key==input:
            return node.key
        elif node.key<input:
            node=node.right
        else:
            ceil=node.key
            node=node.left
    return ceil