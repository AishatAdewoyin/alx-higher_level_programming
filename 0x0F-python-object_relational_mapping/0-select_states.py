#!/usr/bin/python3
import MySQLdb
from sys import argv

'''
a script that lists all states
from hbtn_0e_0_usa database
'''
if __name__ == "__main__":
    sql = MySQLdb.connect(
        host="localhost",
        port=3306, user=argv[1],
        password=argv[2],
        database=argv[3])

    sql_s = sql.cursor()
    sql_s.execute("SELECT * FROM states ORDER BY id ASC")
    db = sql_s.fetchall()
    for states in db:
        print(states)
    sql_s.close()
    db.close()
