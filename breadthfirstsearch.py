def bfs(graph, start, target):
    bfs_queue = [[start, [start]]] # Initialize the Breadth-First Search queue
    visited = set() # Keep track of each vertex visited

    while bfs_queue: # Repeat while the queue is not empty
        current, path = bfs_queue.pop()
        visited.add(current) # Add current vertex to visited
        for i in graph[current]:
            if i not in visited:
                if i is target:
                    return path + [i] # Return the path
                else:
                    bfs_queue.append([i, path + [i]])


graph = {
    'lava': set(['sharks', 'piranhas']),
    'sharks': set(['piranhas', 'bees']),
    'piranhas': set(['bees']),
    'bees': set(['lasers']),
    'lasers': set([])
  }

print(bfs(graph, "lava", "lasers"))