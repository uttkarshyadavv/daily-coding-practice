class Solution(object):
    def dfs(self, i, graph, colour):
        for j in graph[i]:
            if colour[j] == -1:
                colour[j] = 1 - colour[i]
                if not self.dfs(j, graph, colour):
                    return False
            elif colour[j] == colour[i]:
                return False
        return True

    def isBipartite(self, graph):
        rows = len(graph)
        column = len(graph[0])
        colour = [-1] * rows

        for i in range(len(colour)):
            if colour[i] == -1:
                colour[i] = 0
                if not self.dfs(i, graph, colour):
                    return False
        return True
