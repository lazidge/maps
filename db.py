import sqlite3
from store import Node

def create_db(name):
    conn = sqlite3.connect(name + '.db')
    cursor = conn.cursor()
    # Create table
    #print(nodes)
    try:
        cursor.execute('''CREATE TABLE ''' + name + '''(id int, lat decimal, long decimal, neighbors text)''')

        conn.commit()

        # We can also close the connection if we are done with it.
        # Just be sure any changes have been committed or they will be lost.
        conn.close()
        return True
    except(sqlite3.OperationalError):
        conn.close()
        pass

    # Insert a row of data


def update_db(nodes, name):
    conn = sqlite3.connect(name + '.db')
    cursor = conn.cursor()
    #print(nodes)
    if '8140' in nodes:
        print("eat")
    for node in nodes:
        neighbors = '"'
        #command = "INSERT INTO " + name + " VALUES (" + nodes[node].id + ',' + str(nodes[node].lat) + ',' + str(nodes[node].lng) + ',' + neighbors + '"' +  ")"
        if nodes[node].neighbors:
            for neighbor in nodes[node].neighbors:
                neighbors += neighbor + ";"
            neighbors = neighbors[:-1]
        else:
            neighbors = neighbors[:-2]
            neighbors = neighbors + '"'
        #print("INSERT INTO " + name + " VALUES (" + nodes[node].id + ',' + str(nodes[node].lat) + ',' + str(nodes[node].lng) + ',' + neighbors + '"' + ")")
        cursor.execute("INSERT INTO " + name + " VALUES (" + nodes[node].id + ',' + str(nodes[node].lat) + ',' + str(nodes[node].lng) + ',' + neighbors + '"' +  ")")
    conn.commit()
    conn.close()




def get_data(name):
    conn = sqlite3.connect(name + '.db')
    cursor = conn.cursor()
    command = 'SELECT * FROM ' + name
    nodes = {}
    neighbor = {}
    for row in cursor.execute(command):
        #print(row[0])
        nodes[str(row[0])] = Node(row[0], row[1], row[2])
        neighbor[str(row[0])] = row[3]
        if 3730478909 == row[0]:
            print("ayawyyawyawy")
        #print(row[3])


    for node in neighbor:
        nodes[node].neighbors = neighbor[node].split(';')
        if nodes[node].neighbors[0] == '':
            #print(nodes[node].neighbors)
            nodes[node].neighbors.pop()

    #for i in nodes:
        #rint(nodes[i].id, nodes[i].lat, nodes[i].lng, nodes[i].neighbors)
    return nodes

if __name__ == '__main__':
    get_data('dunderhonung')
