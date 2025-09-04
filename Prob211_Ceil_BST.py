def solution(node, val):
    if node is None:
        return None
    if val == node.val:
        return node.val
    elif node.val > val:
        return solution(node.left, val) or node.val
    else:
        return solution(node.right, val)
