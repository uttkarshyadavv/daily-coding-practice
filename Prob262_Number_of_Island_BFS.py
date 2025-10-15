from collections import deque

def island(mat):
    rows = len(mat)
    cols = len(mat[0])
    visited = [[0] * cols for _ in range(rows)]
    count = 0

    def bfs(r, c):
        q = deque()
        q.append((r, c))
        visited[r][c] = 1
        # directions: up, down, left, right, and diagonals
        directions = [(-1,0), (1,0), (0,-1), (0,1), (-1,-1), (-1,1), (1,-1), (1,1)]

        while q:
            x, y = q.popleft()
            for dr, dc in directions:
                nr, nc = x + dr, y + dc
                if (0 <= nr < rows and 0 <= nc < cols and 
                    mat[nr][nc] == 1 and not visited[nr][nc]):
                    visited[nr][nc] = 1
                    q.append((nr, nc))

    for i in range(rows):
        for j in range(cols):
            if mat[i][j] == 1 and not visited[i][j]:
                bfs(i, j)
                count += 1

    return count
