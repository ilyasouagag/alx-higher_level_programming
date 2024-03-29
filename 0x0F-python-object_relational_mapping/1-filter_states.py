#!/usr/bin/python3
"""lists all states from a with a name starting
with N database as argument"""
import MySQLdb
from sys import argv
if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost", user=argv[1],
        passwd=argv[2], database=argv[3], port=3306)
    cu = db.cursor()
    cu.execute(
        "SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY states.id")
    rows = cu.fetchall()
    for row in rows:
        print(row)
    cu.close()
    db.close()
