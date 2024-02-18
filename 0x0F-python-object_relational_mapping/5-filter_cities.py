#!/usr/bin/python3
""" lists all cities from the database hbtn_0e_4_usa"""
import MySQLdb
from sys import argv
if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost", user=argv[1],
        passwd=argv[2], database=argv[3], port=3306)
    cu = db.cursor()
    cu.execute("""SELECT cities.name
               FROM cities LEFT JOIN states on
               states.id = cities.state_id where
               states.name LIKE %s""", (argv[4],))
    rows = cu.fetchall()
    list_to_print = []
    for row in rows:
        list_to_print.append(row[0])
    print(*list_to_print, sep=", ")
    cu.close()
    db.close()
