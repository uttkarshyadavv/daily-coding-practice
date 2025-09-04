mini=float("inf")
def solution(node):
    global mini
    if node is None:
        return 0
    solution(node.left)
    mini=min(mini,node.val)
    solution(node.right)