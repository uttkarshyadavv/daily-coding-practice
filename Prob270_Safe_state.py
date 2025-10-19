from collections import deque
def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        V = len(graph)
        adj_list = [[] for _ in range(V)]
        indegree = [0 for _ in range(V)]

        # Reverse the graph
        for node in range(V):
            for adjnode in graph[node]:
                adj_list[adjnode].append(node)

        # Compute indegrees for reversed graph
        for node in range(V):
            for adjNode in adj_list[node]:
                indegree[adjNode] += 1

        queue = deque()
        result = []

        # Nodes with indegree 0 are initially safe
        for i in range(V):
            if indegree[i] == 0:
                queue.append(i)

        # Kahn’s BFS
        while queue:
            node = queue.popleft()
            result.append(node)
            for adjNode in adj_list[node]:
                indegree[adjNode] -= 1
                if indegree[adjNode] == 0:
                    queue.append(adjNode)

        return sorted(result)