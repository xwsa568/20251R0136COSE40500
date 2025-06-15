def solve_maze(maze, start, end):
    """
    DFS-based maze solver.
    maze: 2D list with 0 as path and 1 as wall
    start: (row, col) tuple
    end: (row, col) tuple
    Returns a list of (row, col) steps from start to end or None if no path.
    """
    rows, cols = len(maze), len(maze[0])
    visited = [[False] * cols for _ in range(rows)]
    path = []

    def dfs(r, c):
        if not (0 <= r < rows and 0 <= c < cols):
            return False
        if maze[r][c] == 1 or visited[r][c]:
            return False
        visited[r][c] = True
        path.append((r, c))
        if (r, c) == end:
            return True
        for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
            if dfs(r + dr, c + dc):
                return True
        path.pop()
        return False

    return path if dfs(start[0], start[1]) else None

if __name__ == "__main__":
    sample_maze = [
        [0,1,0,0,0],
        [0,1,0,1,0],
        [0,0,0,1,0],
        [0,1,1,1,0],
        [0,0,0,0,0],
    ]
    start = (0, 0)
    end = (4, 4)
    print("Path:", solve_maze(sample_maze, start, end))
