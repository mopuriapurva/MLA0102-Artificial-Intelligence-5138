from collections import deque

def bfs(graph, start):
    """
    Perform Breadth-First Search on a graph.

    Parameters:
    graph : dict
        Graph represented as an adjacency list.
    start : any
        The starting node for BFS.
    """
    visited = set()       # To keep track of visited nodes
    queue = deque([start])  # Queue for BFS
    visited.add(start)

    print("BFS Traversal Order:")

    while queue:
        vertex = queue.popleft()
        print(vertex, end=" ")

        # Visit all neighbors
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# Example usage
if __name__ == "__main__":
    # Representing the graph using adjacency list
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }

    start_node = input("Enter the starting node: ").upper()
    
    if start_node not in graph:
        print("Invalid start node!")
    else:
        bfs(graph, start_node)
