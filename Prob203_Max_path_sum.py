maxi=float("-inf")
def solution(node):
    global maxi
    ls=max(0,solution(node.left))
    rs=max(0,solution(node.right))
    maxi=max(maxi,ls+rs+node.val)
    return node.val+max(ls,rs)