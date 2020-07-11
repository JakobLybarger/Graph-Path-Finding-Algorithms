import math
import heapq


def a_star(graph, start, target):
    count = 0
    paths_and_distances = {}
    # Populate each vertex in paths and distances with a distance from start of infinity since the actual distance
    # is unknown
    for vertex in graph:
        paths_and_distances[vertex] = [math.inf, [start.name]]

    paths_and_distances[start][0] = 0  # Set distance from first vertex to self 0
    vertices_to_explore = [(0, start)]  # list of the vertices we need to check
    # While there are vertices to explore and the target is not found
    while vertices_to_explore and paths_and_distances[target][0] == math.inf:
        distance, vertex = heapq.heappop(vertices_to_explore)
        for neighbor, weight in graph[vertex]:
            new_distance = distance + weight + manhattan_heuristic(neighbor, target)  # Euclidean or manhattan distance can
            new_path = paths_and_distances[vertex][1] + [neighbor.name]               # be used depending on what is needed

            if new_distance < paths_and_distances[neighbor][0]:  # If new distance is less than previous difference
                paths_and_distances[neighbor][0] = new_distance  # change in the minheap
                paths_and_distances[neighbor][1] = new_path
                heapq.heappush(vertices_to_explore, (new_distance, neighbor))
                count += 1

    print("Path from {} to {} in {} steps: ".format(start.name, target.name, count), paths_and_distances[target][1])
    return paths_and_distances[target][1]  # Return the path to the target


def manhattan_heuristic(start, target):
    x = abs(start.position[0] - target.position[0])
    y = abs(start.position[1] - target.position[1])
    return x + y


def euclidean_heuristic(start, target):
    x = abs(start.position[0] - target.position[0])
    y = abs(start.position[0] - target.position[0])
    return math.sqrt(x**2 + y**2)
