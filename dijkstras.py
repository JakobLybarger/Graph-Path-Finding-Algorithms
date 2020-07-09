import math
import heapq


def dijkstras(graph, start):
    distances = {}  # Dictionary to keep track of the shortest distance to each vertex in the graph

    # The distance to each vertex is not known so we will just assume each vertex is infinitely far away
    for vertex in graph:
        distances[vertex] = math.inf

    distances[start] = 0  # Distance from the first point to the first point is 0
    vertices_to_explore = [(0, start)]

    # Continue while heap is not empty
    while vertices_to_explore:
        distance, vertex = heapq.heappop(vertices_to_explore)  # Pop the minimum distance vertex off of the heap

        for neighbor, e_weight in graph[vertex]:
            new_distance = distance + e_weight

            # If the new distance is less than the current distance set the current distance as new distance
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                heapq.heappush(vertices_to_explore, (new_distance, neighbor))

    return distances  # The dictionary of minimum distances from start to each vertex


graph = {
        'A': [('B', 10), ('C', 3)],
        'C': [('D', 2)],
        'D': [('E', 10)],
        'E': [('A', 7)],
        'B': [('C', 3), ('D', 2)]
    }

print(dijkstras(graph, "A"))