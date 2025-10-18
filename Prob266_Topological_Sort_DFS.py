#Topological Sort (DFS)
#Ordering of nodes in such a way that if there is an edge between u and v, u should appear before v in that ordering
#Graph Should be Directed Acyclic Graph (DAG)
class Solution:
    def dfs(self, node, adj, visited, stack):
        visited[node] = 1
        for adjNode in adj[node]:
            if not visited[adjNode]:
                self.dfs(adjNode, adj, visited, stack)
        stack.append(node)

    def topoSort(self, V, edges):
        # Build adjacency list for a directed graph
        adj = [[] for _ in range(V)]
        for u, v in edges:
            adj[u].append(v)
        
        visited = [0] * V
        stack = []
        
        for i in range(V):
            if not visited[i]:
                self.dfs(i, adj, visited, stack)
        
        # Reverse stack for topological order
        return stack[::-1]
