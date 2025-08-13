from collections import deque

def minStepsToTreasure(grid):
    rows, cols = len(grid), len(grid[0])
    visited = [[False]*cols for _ in range(rows)]
    q = deque()

    # find start 'S'
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 'S':
                q.append((r, c, 0))
                visited[r][c] = True

    directions = [(1,0),(-1,0),(0,1),(0,-1)]

    while q:
        r, c, steps = q.popleft()
        if grid[r][c] == 'T':
            return steps
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc] and grid[nr][nc] != 'X':
                visited[nr][nc] = True
                q.append((nr, nc, steps + 1))
    return -1

# Example
grid = [
    ['S','O','O','S','S'],
    ['X','O','X','O','X'],
    ['O','O','O','O','X'],
    ['X','X','X','O','O'],
    ['X','X','X','X','T']
]
print(minStepsToTreasure(grid))  # Output: steps to T
