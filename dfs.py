# Depth First Search (DFS) Implementation
# Author: Your Name

def dfs_recursive(graph, node, visited=None):
    """
    Recursive implementation of DFS.
    
    Parameters:
    graph (dict): Adjacency list representation of graph
    node (str/int): Starting node
    visited (set): Set to keep track of visited nodes
    """
    
    if visited is None:
        visited = set()

    if node not in visited:
        print(node, end=" ")
        visited.add(node)

        for neighbor in graph[node]:
            dfs_recursive(graph, neighbor, visited)

    return visited


if __name__ == "__main__":
    
    # Example Graph (Adjacency List)
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': [],
        'F': []
    }

    print("DFS Traversal starting from node A:")
    dfs_recursive(graph, 'A')