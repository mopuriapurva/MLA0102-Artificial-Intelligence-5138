from collections import deque

# Directions: up, down, left, right
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# Sample grid: 0 = clean, 1 = dirty
# You can change the grid size or dirty cells
grid = [
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [1, 0, 0, 0],
    [0, 0, 0, 1]
]

ROWS = len(grid)
COLS = len(grid[0])

# Vacuum starting position
vacuum_pos = (0, 0)

# Function to check if a cell is inside the grid
def in_bounds(x, y):
    return 0 <= x < ROWS and 0 <= y < COLS

# BFS to find shortest path to nearest dirty cell
def bfs(start):
    visited = set()
    queue = deque()
    queue.append((start, [start]))  # position and path
    visited.add(start)

    while queue:
        (x, y), path = queue.popleft()
        if grid[x][y] == 1:  # Found dirty cell
            return path
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if in_bounds(nx, ny) and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append(((nx, ny), path + [(nx, ny)]))
    return None

# Function to simulate vacuum cleaning
def clean_grid(vacuum_pos):
    total_moves = 0
    path_taken = []

    while any(1 in row for row in grid):
        path_to_dirty = bfs(vacuum_pos)
        if not path_to_dirty:
            break  # No reachable dirty cell

        # Move vacuum along the path
        for pos in path_to_dirty[1:]:  # Skip starting position
            vacuum_pos = pos
            path_taken.append(pos)
            total_moves += 1
            x, y = pos
            if grid[x][y] == 1:
                grid[x][y] = 0  # Clean the cell
                print(f"Cleaned cell at {pos}")
    
    print("\nAll dirty cells cleaned!")
    print(f"Total moves taken: {total_moves}")
    print(f"Path taken: {path_taken}")

# Run the simulation
clean_grid(vacuum_pos)
