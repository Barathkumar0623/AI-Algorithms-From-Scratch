import heapq

def a_star(graph, heuristics, start, goal):
    open_list = []
    heapq.heappush(open_list, (0, start))
    
    g_cost = {start: 0}
    parent = {start: None}
    
    closed = set()
    
    while open_list:
        current_f, current = heapq.heappop(open_list)
        
        if current == goal:
            path = []
            while current:
                path.append(current)
                current = parent[current]
            return path[::-1]
        
        closed.add(current)
        
        for neighbor, cost in graph[current]:
            if neighbor in closed:
                continue
                
            new_g = g_cost[current] + cost
            
            if neighbor not in g_cost or new_g < g_cost[neighbor]:
                g_cost[neighbor] = new_g
                f = new_g + heuristics[neighbor]
                heapq.heappush(open_list, (f, neighbor))
                parent[neighbor] = current
    
    return None


# Graph representation
graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 5)],
    'C': [('D', 1)],
    'D': []
}

# Heuristic values
heuristics = {
    'A': 3,
    'B': 4,
    'C': 2,
    'D': 0
}

# Run A*
path = a_star(graph, heuristics, 'A', 'D')
print("Shortest Path:", path)