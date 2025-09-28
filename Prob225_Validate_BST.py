def solution(self,node,limit):
    if node is None:
        return True
    if not limit[0]<node.val<limit[1]:
        return False
    left=self.solve(node.left,[limit[0],node.val])
    if left==False:
        return False
    right=self.solve(node.right,[node.val,limit[1]])
    return left and right
solution(node,[float(-"inf"),float("inf")])
