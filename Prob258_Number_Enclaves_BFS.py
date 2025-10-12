from collections import deque

def enclave(mat):
    rows = len(mat)
    column = len(mat[0])
    queue = deque()
    count1 = 0
    visited = [[0]*column for _ in range(rows)]

    # push all boundary lands into queue and mark them visited
    for r in range(rows):
        for c in range(column):
            if r == 0 or c == 0 or r == rows-1 or c == column-1:
                if mat[r][c] == 1 and visited[r][c] == 0:
                    queue.append((r, c))
                    visited[r][c] = 1
                    count1 += 1  # include the boundary cell itself

    # BFS to mark all lands connected to boundary
    while queue:
        r, c = queue.popleft()
        for x, y in ((0,1),(1,0),(0,-1),(-1,0)):
            new_r = r + x
            new_c = c + y
            if new_r < 0 or new_r >= rows or new_c < 0 or new_c >= column:
                continue
            if visited[new_r][new_c] == 1:
                continue
            if mat[new_r][new_c] == 1:
                queue.append((new_r, new_c))
                visited[new_r][new_c] = 1
                count1 += 1  # include this cell

    # total land cells
    total1 = 0
    for r in range(rows):
        for c in range(column):
            if mat[r][c] == 1:
                total1 += 1

    return total1 - count1
