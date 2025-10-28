from collections import deque

def water_jug_problem():
    visited = set()
    queue = deque()

    # (4-gallon, 3-gallon)
    queue.append((0, 0))

    print("Steps to get exactly 2 gallons in the 4-gallon jug:\n")

    while queue:
        x, y = queue.popleft()
        if (x, y) in visited:
            continue
        visited.add((x, y))
        print(f"({x}, {y})")

        # Goal state
        if x == 2:
            print("\n✅ Reached the goal state (2 gallons in the 4-gallon jug)!")
            return

        # Possible moves
        next_states = set()
        next_states.add((4, y))              # Fill 4-gallon jug
        next_states.add((x, 3))              # Fill 3-gallon jug
        next_states.add((0, y))              # Empty 4-gallon jug
        next_states.add((x, 0))              # Empty 3-gallon jug

        # Pour 4 → 3
        pour = min(x, 3 - y)
        next_states.add((x - pour, y + pour))

        # Pour 3 → 4
        pour = min(y, 4 - x)
        next_states.add((x + pour, y - pour))

        for state in next_states:
            if state not in visited:
                queue.append(state)


if __name__ == "__main__":
    water_jug_problem()
