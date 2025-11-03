import heapq
class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type k: int
        :rtype: int
        """
        adj=[[] for _ in range(n)]
        for u,v,w in flights:
            adj[u].append((v,w))

        max_flights = k + 1              # you can take up to k+1 flights
        # best[node][f] = min cost to reach node using exactly f flights
        best = [[float('inf')] * (max_flights + 1) for _ in range(n)]
        heap = [(0, src, 0)]  # (cost, node, flights_used)
        best[src][0] = 0

        while heap:
            cost,u,fl = heapq.heappop(heap)
            # if reached destination within allowed flights -> done
            if u == dst:
                return cost
            # if we've already used all allowed flights, can't go further
            if fl == max_flights:
                continue
            # if this state is worse than stored, skip
            if cost > best[u][fl]:
                continue
            for v,wt in adj[u]:
                nc = cost + wt
                nfl = fl + 1
                # if we can improve best[v] when using nfl flights, push
                if nc < best[v][nfl]:
                    best[v][nfl] = nc
                    heapq.heappush(heap, (nc, v, nfl))

        return -1
