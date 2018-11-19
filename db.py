import sqlite3
from store import Node

def create_db(name):
    conn = sqlite3.connect(name + '.db')
    cursor = conn.cursor()
    try:
        cursor.execute('''CREATE TABLE ''' + name + '''(id int, lat decimal, long decimal, neighbors text)''')
        conn.commit()
        conn.close()
        return True
    except(sqlite3.OperationalError):
        conn.close()
        pass

def update_db(nodes, name):
    conn = sqlite3.connect(name + '.db')
    cursor = conn.cursor()
    command = []
    for node in nodes:
        neighbors = ":".join(nodes[node].neighbors)
        command.append((nodes[node].id, nodes[node].lat, nodes[node].lng, neighbors))
    #print("INSERT INTO " + name + " VALUES (" + nodes[node].id + ',' + str(nodes[node].lat) + ',' + str(nodes[node].lng) + ',"' + neighbors + '"' + ")")
    cursor.executemany("INSERT INTO " + name + " VALUES (?,?,?,?)", command)
    conn.commit()
    conn.close()

def get_data(name):
    conn = sqlite3.connect(name + '.db')
    cursor = conn.cursor()
    command = 'SELECT * FROM ' + name
    nodes = {}
    neighbor = {}
    for row in cursor.execute(command):
        nodes[str(row[0])] = Node(row[0], row[1], row[2])
        neighbor[str(row[0])] = row[3]
    for node in neighbor:
        nodes[node].neighbors = neighbor[node].split(':')
        #if nodes[node].neighbors[0] == '':
        #    nodes[node].neighbors.pop()
    return nodes

if __name__ == '__main__':
    get_data('dunderhonung')
