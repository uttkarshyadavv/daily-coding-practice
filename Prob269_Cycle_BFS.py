from collections import deque
def cycle(V,edge):
    adj_list=[[] for _ in range(V)]
    indegrees=[[0] for _ in range(V)]
    for u,v in edge:
        indegrees[v]+=1
        adj_list[u].append(v)
        adj_list[v].append(u)
    queue=deque()
    for i in range(V):
        if indegrees[i]==0:
            queue.append(i)
    count=0
    while len(queue)!=0:
        current_node=queue.popleft()
        count+=1
        for adjNode in adj_list[current_node]:
            indegrees[adjNode]-=1
            if indegrees[adjNode]==0:
                queue.append(adjNode)
    if count!=V:
        return True
    else:
        return False

    
