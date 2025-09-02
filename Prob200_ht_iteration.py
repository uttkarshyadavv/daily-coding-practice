from collections import deque

def level_order(root):
    queue=deque([])
    height=0
    queue.append(root)
    while len(queue)!=0:
        level_size=len(queue)
        height+=1
        for _ in range(level_size):
            e=queue.popleft()
            if e.left is not None:
                queue.append(e.left)
            if e.right is not None:
                queue.append(e.right)
    return height