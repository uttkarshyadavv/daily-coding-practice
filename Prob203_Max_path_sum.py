maxi=float("-inf")
def solution(node):
    global maxi
    if node is None:
        return 0
    ls=max(0,solution(node.left))
    rs=max(0,solution(node.right))
    maxi=max(maxi,ls+rs+node.val)
    return node.val+max(ls,rs)