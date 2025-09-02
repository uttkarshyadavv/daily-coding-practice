def solution(node):
    Lh=solution(node.left)
    Rh=solution(node.right)
    diff=abs(Lh-Rh)
    if diff>1:
        return False
    return 1+max(Lh,Rh)
    
