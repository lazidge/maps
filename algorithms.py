import math
from heapq import heapify, heappop, heappush
from collections import defaultdict
from store import Node

def length_haversine(p1, p2):
    lat1 = p1.lat
    lng1 = p1.lng
    lat2 = p2.lat
    lng2 = p2.lng
    lat1, lng1, lat2, lng2 = map(math.radians, [lat1, lng1, lat2, lng2])
    dlat = lat2 - lat1
    dlng = lng2 - lng1
    a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlng / 2) ** 2
    c = 2 * math.asin(math.sqrt(a))

    return 6372797.560856 * c # return the distance in meters

def get_closest_node_id(nodes, source_node):
    """ Search through all nodes and return the id of the node
    that is closest to 'source_node'. """
    shortest_distance = float('Inf')
    closest_node_id = 0
    for node in nodes:
        if length_haversine(nodes[node], source_node) <= shortest_distance:
            shortest_distance = length_haversine(nodes[node], source_node)
            closest_node_id = node
    return closest_node_id

def find_shortest_path(nodes, source_id, target_id):
    """ Return the shortest path using Dijkstra's algortihm. """
    shortest_path = []
    paths = defaultdict(lambda: [])
    shortest_distance = float('Inf')
    queue = []
    heapify(queue)
    visited = set()
    shortest_distances = defaultdict(lambda: float('inf'))
    nodes[source_id].distance = 0
    heappush(queue, (nodes[source_id]))
    shortest_distances[nodes[source_id]] = 0
    while queue:
        node = heappop(queue)
        print('wat')
        if node == nodes[target_id]:
            shortest_path = paths[node]
            shortest_distance = shortest_distances[node]
            break
        elif not node in visited:
            visited.add(node)
            #print(node)
            for neighbor in node.neighbors:
                if length_haversine(node, nodes[neighbor]) + shortest_distances[node] < shortest_distances[neighbor]:
                    shortest_distances[neighbor] = length_haversine(node, nodes[neighbor]) + shortest_distances[node]
                    #print(shortest_distances[neighbor])
                    nodes[neighbor].distance = shortest_distances[neighbor]
                    heappush(queue, (nodes[neighbor]))
                    paths[neighbor] = paths[node].append(neighbor)
    print(shortest_path)
    return shortest_path
