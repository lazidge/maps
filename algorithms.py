import math
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

    nodes[source_id].neighbors
    return []
