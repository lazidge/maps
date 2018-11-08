from lib import run_server, get
from lib import read_html
from lib import post
from store import Node, extract_osm_nodes, add_neighbors
from algorithms import get_closest_node_id, find_shortest_path
import json

nodes = extract_osm_nodes('linkoping.osm')
nodes = add_neighbors(nodes)


@get('/')
def index():
     return read_html('templates/index.html')

@post('/shortest-path')
def shortest_path(body):
    body = json.loads(body)
    source_id = get_closest_node_id(nodes, Node('-1', body['lat1'], body['lng1']))
    target_id = get_closest_node_id(nodes, Node('-1', body['lat2'], body['lng2']))
    path = find_shortest_path(nodes, source_id, target_id)
    for i in range(len(path)):
        node_id = path[i]
        path[i] = (nodes[node_id].lat, nodes[node_id].lng)
    response = {'path': path} # The front-end expects the response to have a 'path' key
    return json.dumps(response)

run_server(2222)
