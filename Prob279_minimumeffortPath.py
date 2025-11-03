import heapq

class Solution(object):
    def minimumEffortPath(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: int
        """
        n = len(heights)
        m = len(heights[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # min_effort[r][c] = minimum effort needed to reach (r, c)
        min_effort = [[float('inf')] * m for _ in range(n)]
        min_effort[0][0] = 0

        # Min-heap: (effort, row, col)
        heap = [(0, 0, 0)]

        while heap:
            eff, r, c = heapq.heappop(heap)

            # If we reached destination, return current effort
            if r == n - 1 and c == m - 1:
                return eff

            # If this path is already worse than known one, skip
            if eff > min_effort[r][c]:
                continue

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < m:
                    diff = abs(heights[nr][nc] - heights[r][c])
                    new_eff = max(eff, diff)
                    if new_eff < min_effort[nr][nc]:
                        min_effort[nr][nc] = new_eff
                        heapq.heappush(heap, (new_eff, nr, nc))

        return 0
