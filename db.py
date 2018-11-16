import sqlite3
from store import Node

def create_db(nodes, name):
    conn = sqlite3.connect(name + '.db')
    cursor = conn.cursor()
    # Create table
    #print(nodes)
    try:
        cursor.execute('''CREATE TABLE ''' + name + '''(id int, lat decimal, long decimal, neighbors text)''')
    except(sqlite3.OperationalError):
        pass

    # Insert a row of data
    command = "INSERT INTO " + name + " VALUES (" + nodes[node].id + ',' + str(nodes[node].lat) + ',' + str(nodes[node].lng) + ',' + neighbors + '"' +  ")"
    for node in nodes:
        neighbors = '"'
        for neighbor in nodes[node].neighbors:
            neighbors += neighbor + ";"
        #print("INSERT INTO " + name + " VALUES (" + nodes[node].id + ',' + str(nodes[node].lat) + ',' + str(nodes[node].lng) + ',' + neighbors + '"' + ")")
        cursor.execute(command)

    # Save (commit) the changes
    conn.commit()

    # We can also close the connection if we are done with it.
    # Just be sure any changes have been committed or they will be lost.
    conn.close()

def get_data(name):
    conn = sqlite3.connect(name + '.db')
    cursor = conn.cursor()
    command = 'SELECT * FROM ' + name + ' ORDER BY id'
    for row in cursor.execute(command):
        print(row)
