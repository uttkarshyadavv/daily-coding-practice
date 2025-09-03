from collections import deque
def solution(root):
    result=[]
    queue=deque([])
    queue.append(root)
    while len(queue)!=0:
        level_size=len(queue)
        for i in range(level_size):
            node=queue.popleft()
            if i==level_size-1:
                result.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return result
