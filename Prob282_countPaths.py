import heapq
def countPaths(n,roads):
    mod=10**9 +7
    adj_list=[]*n
    for u,v,time in roads:
        adj_list[u].append(v,time)
        adj_list[v].append(u,time)
    
    dist= [float("inf")]*n
    ways=[0]*n
    dist[0]=0
    ways[0]=1

    pq=[(0,0)]
    while pq:
        curr_time, node= heapq.heappop(pq)

        if curr_time> dist[node]:
            continue

        for nxt_intersection, time in adj_list[node]:
            new_time= curr_time+time

            if new_time < dist[nxt_intersection]:
                dist[nxt_intersection]= new_time
                ways[nxt_intersection]= ways[node]
                heapq.heappush(pq,(new_time,nxt_intersection))
            elif new_time==dist[nxt_intersection]:
                ways[nxt_intersection]= (ways[nxt_intersection]+ways[node])%mod
    return ways[n-1]%mod

            
