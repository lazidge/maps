class Node:
    def __init__(self, id, lat, lng):
        self.id = id
        self.lat = float(lat)
        self.lng = float(lng)
        self.distance = float()
        self.neighbors = [] # list of node ids: ['4242', '3141592', '65358979'...]

    def __lt__(self, other_heap_item):
        return self.distance < other_heap_item.distance # We want to rank by distance

from osm_parser import get_default_parser
from store import Node

parser = None # Have a global reusable parser object

def extract_osm_nodes(f_name):
    global parser
    parser = get_default_parser(f_name)
    nodes = dict()

    for node in parser.iter_nodes():
        nodes[node['id']] = Node(node['id'], node['lat'], node['lon'])

    return nodes

def add_neighbors(nodes):
    for way in parser.iter_ways():
        road = way['road']
        tags = way['tags']
        if 'highway' in tags: #and not 'pedestrian' in tags and not 'cycleway' in tags and not 'path' in tags: and not 'footway' in tags and not 'cycleway' in tags and not 'path' in tags and not 'steps' in tags and not 'track' in tags and not 'sidewalk' in tags:
            for i in range(len(road) - 1):
                node1 = road[i]
                node2 = road[i+1]
                nodes[node1].neighbors.append(node2)
                nodes[node2].neighbors.append(node1)
    return nodes
        # node1 and node2 forms a bidirectional EDGE
