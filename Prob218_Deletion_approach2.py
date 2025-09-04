def solution(node,val):
    if node.val>val:
        return solution(node.left,val)
    elif node.val<val:
        return solution(node.right,val)
    else:
        if node.left is None:
            return node.right
        if node.right is None:
            return node.left
        else:
            temp=node.right
            while temp.left:
                temp=temp.left
            temp.left=node.left
            return node.right