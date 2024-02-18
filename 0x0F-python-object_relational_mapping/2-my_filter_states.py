#!/usr/bin/python3
"""displays all values in the states table
of hbtn_0e_0_usa where name matches the argument"""
import MySQLdb
from sys import argv
if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost", user=argv[1],
        passwd=argv[2], database=argv[3], port=3306)
    cu = db.cursor()
    cu.execute(
        "SELECT * FROM states WHERE name LIKE BINARY '{}' "
        "ORDER BY states.id".format(argv[4])
    )
    rows = cu.fetchall()
    for row in rows:
        print(row)
    cu.close()
    db.close()
