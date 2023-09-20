#!/usr/bin/python3
"""
lists all cities from the database hbtn_0e_4_usa
"""
if __name__ == "__main__":

    import MySQLdb
    from sys import argv

    sql = MySQLdb.connect(host="localhost",
                          port=3306,
                          user=argv[1],
                          passwd=argv[2],
                          db=argv[3],
                          charset="utf8")
    sql_s = sql.cursor()
    sql_s.execute("""SELECT cities.id, cities.name, states.name
    FROM cities
    LEFT JOIN states ON cities.state_id = states.id
    ORDER BY cities.id ASC""")
    db = sql_s.fetchall()
    for states in db:
        print(states)
    sql_s.close()
    sql.close()
