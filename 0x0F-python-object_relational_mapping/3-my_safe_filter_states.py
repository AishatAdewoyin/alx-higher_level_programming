#!/usr/bin/python3
'''
script that lists all states from the database
where name matches
'''

import MySQLdb
from sys import argv

if __name__ == "__main__":
    sql = MySQLdb.connect(
        host="localhost", port=3306, user=argv[1],
        password=argv[2], database=argv[3])
    sql_s = sql.cursor()
    sql_s.execute(
        "SELECT * FROM states WHERE name LIKE %s ORDER BY id ASC",
        (argv[4],)
        )
    db = sql_s.fetchall()
    for i in db:
        print(i)
