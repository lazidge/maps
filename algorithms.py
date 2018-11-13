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

class HeapItem:
    def __init__(self, node_id, distance, path):
        self.node_id = node_id
        self.distance = distance
        self.path = path
    def __lt__(self, other_heap_item):
        self.distance < other_heap_item.distance

def find_shortest_path(nodes, source_id, target_id):
    """ Return the shortest path using Dijkstra's algorithm. """
    shortest_path = []
    #paths = defaultdict(lambda: [])
    shortest_distance = float('Inf')
    queue = []
    heapify(queue)
    visited = set()
    shortest_distances = defaultdict(lambda: float('inf'))
    shortest_distances[source_id] = 0
    heappush(queue, HeapItem(source_id, 0, []))
    shortest_distances[nodes[source_id]] = 0
    while queue:
        node = heappop(queue)
        if node.node_id == target_id:
            shortest_path = node.path
            last = float('Inf')
            """for i in node:
                if i.distance < last:
                    last = i"""
            shortest_distance = nodes[node.node_id].distance
            print("yeet")
            break
        elif not node.node_id in visited:
            visited.add(node.node_id)
            #print(visited)
            #print(node)
            for neighbor in nodes[node.node_id].neighbors:
                if (shortest_distances[node.node_id] + length_haversine(nodes[node.node_id], nodes[neighbor])) <= shortest_distances[neighbor]:
                    shortest_distances[neighbor] = shortest_distances[node.node_id] + length_haversine(nodes[node.node_id], nodes[neighbor])
                    neighbor_path = node.path.copy()
                    neighbor_path.append(neighbor)
                    heappush(queue, HeapItem(neighbor, shortest_distances[neighbor], neighbor_path))
    #print(shortest_path)
    return shortest_path
