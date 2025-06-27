#!/usr/bin/python3
"""
Lists all values in the states table where name matches the argument.
"""

import MySQLdb
import sys

if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cur = db.cursor()

    query = (
        "SELECT * FROM states "
        "WHERE name = BINARY '{}' "
        "ORDER BY id ASC".format(state_name)
    )

    cur.execute(query)

    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()
