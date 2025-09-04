mini=float("inf")
def solution(node):
    global mini
    if node is None:
        return
    solution(node.left)
    mini=min(mini,node.val)