maxi=0
def solution(node):
    global maxi
    if node is None:
        return 0
    left=solution(node.left)
    right=solution(node.right)
    maxi=max(maxi,left+right)
    return 1+max(left,right)