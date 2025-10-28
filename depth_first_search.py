def dfs(graph, start, visited=None):
    """
    Perform Depth-First Search on a graph.
    """
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=" ")

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)


# Example usage
if __name__ == "__main__":
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }

    start_node = input("Enter the starting node: ").upper()

    if start_node not in graph:
        print("Invalid node!")
    else:
        print("DFS Traversal Order:")
        dfs(graph, start_node)
