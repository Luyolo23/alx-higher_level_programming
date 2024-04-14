#!/usr/bin/python3
<<<<<<< HEAD
""" Script that lists all states from the database hbtn_0e_0_usa """
import MySQLdb
from sys import argv

# The code should not be executed when imported
if __name__ == '__main__':

    # make a connection to the database
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    # It gives us the ability to have multiple seperate working environments
    # through the same connection to the database.
    cur = db.cursor()
    cur.execute("SELECT * FROM states")

    rows = cur.fetchall()
    for i in rows:
        print(i)
    # Clean up process
    cur.close()
    db.close()
=======
"""
This script lists all states from the
database `hbtn_0e_0_usa`.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Access to the database and get the states
    from the database.
    """
    db_connect = MySQLdb.connect(
        host="localhost", user=argv[1], port=3306, passwd=argv[2], db=argv[3])

    db_cursor = db_connect.cursor()

    db_cursor.execute("SELECT * FROM states")

    rows_selected = db_cursor.fetchall()

    for row in rows_selected:
        print(row)
>>>>>>> 0a38a780a46132dd3040c7cdef82089acfded375
