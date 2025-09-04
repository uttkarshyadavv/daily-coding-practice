#Binary search Tree: Left<=Node<=Right
#Time Complexity=O(logn)
#Search
#In This The height is normally O(logn) [Special Case Exist] 
def solution(node,val):
    if node is None:
        return None
    if val>node.val:
        return solution(node.right,val)
    elif val<node.val:
        return solution(node.left,val)
    elif node.val==val:
        return node

    