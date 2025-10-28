import heapq

# Goal state
goal_state = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 0]]  # 0 represents the empty space

# Helper functions
def find_position(state, value):
    """Find the position (row, col) of a tile value in a given state."""
    for i in range(3):
        for j in range(3):
            if state[i][j] == value:
                return i, j

def manhattan_distance(state):
    """Heuristic: sum of Manhattan distances between tiles and their goal positions."""
    distance = 0
    for i in range(3):
        for j in range(3):
            value = state[i][j]
            if value != 0:
                goal_i, goal_j = find_position(goal_state, value)
                distance += abs(i - goal_i) + abs(j - goal_j)
    return distance

def get_neighbors(state):
    """Generate all possible states by sliding a tile into the empty space."""
    neighbors = []
    x, y = find_position(state, 0)  # Find empty tile
    directions = [(-1,0), (1,0), (0,-1), (0,1)]  # Up, Down, Left, Right
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            # Swap empty tile with the neighboring tile
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            neighbors.append(new_state)
    return neighbors

def state_to_tuple(state):
    """Convert list of lists to tuple of tuples (hashable for set/dict)."""
    return tuple(tuple(row) for row in state)

def print_state(state):
    """Pretty-print the puzzle state."""
    for row in state:
        print(' '.join(str(x) if x != 0 else ' ' for x in row))
    print()

def a_star(start_state):
    """Solve the 8-puzzle using the A* search algorithm."""
    open_list = []
    heapq.heappush(open_list, (manhattan_distance(start_state), 0, start_state, []))
    visited = set()

    while open_list:
        est_total_cost, cost, state, path = heapq.heappop(open_list)

        if state == goal_state:
            return path + [state]

        visited.add(state_to_tuple(state))

        for neighbor in get_neighbors(state):
            if state_to_tuple(neighbor) not in visited:
                heapq.heappush(open_list, (
                    cost + 1 + manhattan_distance(neighbor),
                    cost + 1,
                    neighbor,
                    path + [state]
                ))
    return None

# Example usage
if __name__ == "__main__":
    start_state = [[1, 2, 3],
                   [4, 0, 6],
                   [7, 5, 8]]

    print("Initial State:")
    print_state(start_state)

    solution = a_star(start_state)

    if solution:
        print(f"Solution found in {len(solution)-1} moves:\n")
        for step in solution:
            print_state(step)
    else:
        print("No solution exists for this configuration.")
