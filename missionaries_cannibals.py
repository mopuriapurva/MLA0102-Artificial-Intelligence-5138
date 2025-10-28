from collections import deque

# Define the initial state
# (missionaries_left, cannibals_left, boat_position)
# boat_position: 0 = left side, 1 = right side
initial_state = (3, 3, 0)
goal_state = (0, 0, 1)

# Function to check if a state is valid
def is_valid(state):
    m_left, c_left, _ = state
    m_right = 3 - m_left
    c_right = 3 - c_left
    
    # Check for negative numbers
    if m_left < 0 or c_left < 0 or m_right < 0 or c_right < 0:
        return False
    
    # Check for missionaries being outnumbered by cannibals
    if (m_left > 0 and m_left < c_left) or (m_right > 0 and m_right < c_right):
        return False
    
    return True

# Generate all possible next states
def get_next_states(state):
    m, c, boat = state
    moves = []
    # Possible number of missionaries and cannibals to move
    for m_move in range(3):
        for c_move in range(3):
            if 1 <= m_move + c_move <= 2:  # Boat carries 1 or 2 people
                if boat == 0:  # Boat on left side
                    new_state = (m - m_move, c - c_move, 1)
                else:          # Boat on right side
                    new_state = (m + m_move, c + c_move, 0)
                
                if is_valid(new_state):
                    moves.append(new_state)
    return moves

# BFS search to find solution
def bfs(initial_state):
    queue = deque()
    queue.append([initial_state])
    visited = set()
    visited.add(initial_state)
    
    while queue:
        path = queue.popleft()
        current_state = path[-1]
        
        if current_state[:3] == goal_state:
            return path
        
        for next_state in get_next_states(current_state):
            if next_state not in visited:
                visited.add(next_state)
                new_path = list(path)
                new_path.append(next_state)
                queue.append(new_path)
    return None

# Run BFS to find solution
solution = bfs(initial_state)

# Display solution
if solution:
    print("Solution found! Steps:")
    for i, state in enumerate(solution):
        m_left, c_left, boat = state
        m_right = 3 - m_left
        c_right = 3 - c_left
        side = 'left' if boat == 0 else 'right'
        print(f"Step {i}: Left side -> M:{m_left}, C:{c_left} | Right side -> M:{m_right}, C:{c_right} | Boat: {side}")
else:
    print("No solution found.")
