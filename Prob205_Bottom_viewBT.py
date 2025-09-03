#Left side is given priority
from collections import deque
def bottomView(self,root):
    if not root:
        return None
    ans=[]
    queue=deque()
    result={}
    queue.append(root,0)
    while queue:
        e,line=queue.popleft()
        result[line]=e.data
        if e.left:
            queue.append((e.left,line-1))
        if e.right:
            queue.append((e.right,line+1))
    for value in sorted(result.items()):
        ans.append(value[1])
    return ans
        