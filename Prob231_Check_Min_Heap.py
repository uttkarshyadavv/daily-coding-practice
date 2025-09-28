def solution(node):
    if node is None:
        return True
    if node.left and node.val > node.left.val:
        return False
    if node.right and node.val > node.right.val:
        return False
    return solution(node.left) and solution(node.right)