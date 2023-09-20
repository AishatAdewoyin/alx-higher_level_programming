#!/usr/bin/python3
"""
Lists all states with names starting with 'N'
from the database hbtn_0e_0_usa.
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    sql = MySQLdb.connect(
        host="localhost", port=3306, user=argv[1],
        password=argv[2], database=argv[3])
    sql_s = sql.cursor()
    sql_s.execute(
        "SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC")
    db = sql_s.fetchall()
    for states in db:
        print(states)
