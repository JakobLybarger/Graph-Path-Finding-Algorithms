def dfs(graph, current, target, visited=None):
    # If visited is None create a list
    if not visited:
        visited = []
    visited.append(current) # Append current vertex to list
    if current is target:
        # If current vertex is target return visited
        return visited

    for i in graph[current]:
        if i not in visited:
            path = dfs(graph, i, target, visited)
            if path:
                return path


graph = {
    'lava': set(['sharks', 'piranhas']),
    'sharks': set(['piranhas', 'bees']),
    'piranhas': set(['bees']),
    'bees': set(['lasers']),
    'lasers': set([])
  }

print(dfs(graph, "sharks", "lasers"))