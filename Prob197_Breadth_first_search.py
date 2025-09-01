from collections import deque
#Breadth first order
#Level Order Traversal
def levelorder(node):
    result=[]
    queue=deque([])
    queue.append(node)
    while len(queue)!=0:
        e=queue.popleft()
        result.append(e.data)
        if e.left is not None:
            queue.append(e.left)
        if e.right is not None:
            queue.append(e.right)
    return result