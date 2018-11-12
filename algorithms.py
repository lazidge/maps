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
    paths = defaultdict(lambda: [])
    shortest_distance = float('Inf')
    queue = []
    heapify(queue)
    visited = set()
    shortest_distances = defaultdict(lambda: float('inf'))
    nodes[source_id].distance = 0
    heappush(queue, HeapItem(source_id, 0, []))
    shortest_distances[nodes[source_id]] = 0
    while queue:
        node = heappop(queue)
        #print(nodes[target_id])
        if node.node_id == target_id:
            shortest_path = node.path
            shortest_distance = shortest_distances[node]
            print("yeet")
            break
        elif not node.node_id in visited:
            visited.add(node.node_id)
            #print(visited)
            #print(node)
            for neighbor in nodes[node.node_id].neighbors:
                if (shortest_distances[node.node_id] + length_haversine(nodes[node.node_id], nodes[neighbor])) <= shortest_distances[neighbor]:
                    shortest_distances[neighbor] = shortest_distances[node.node_id] + length_haversine(nodes[node.node_id], nodes[neighbor])
                    nodes[neighbor].distance = shortest_distances[neighbor]
                    temp = node.path
                    temp.append(neighbor)
                    #print(temp)
                    heappush(queue, HeapItem(neighbor, nodes[neighbor].distance, temp))
                    #paths[neighbor].append(neighbor)
                    #if neighbor == target_id:
                    #print(str(neighbor), ": ", str(paths[neighbor]))
                    #print(paths[neighbor])
    #print(shortest_path)
    return shortest_path
