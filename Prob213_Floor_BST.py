def solution(node, val):
    if node is None:
        return None
    if val == node.val:
        return node.val
    elif node.val < val:
        return solution(node.right, val) or node.val
    else:  # node.val > val
        return solution(node.left, val)
