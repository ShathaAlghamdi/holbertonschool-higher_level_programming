#!/usr/bin/python3
"""filter states by user input."""

import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cursor = db.cursor()
    cursor.execute(
    "SELECT * FROM states WHERE name = '{}' "
    "ORDER BY states.id ASC".format(sys.argv[4])
   )
    for row in cursor.fetchall():
        print(row)

    cursor.close()
    db.close()