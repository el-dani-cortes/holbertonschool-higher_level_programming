#!/usr/bin/python3
"""
Script that takes in the name of a state as an argument and lists all cities
of that state, using the database hbtn_0e_4_usa.
"""
import MySQLdb as mdb
import sys


if __name__ == "__main__":
    args = {
        "host": "localhost",
        "port": 3306,
        "user": sys.argv[1],
        "passwd": sys.argv[2],
        "db": sys.argv[3],
        "charset": "utf8"
        }
    d_base = sys.argv
    try:
        conn = mdb.connect(**args)
        cur = conn.cursor()
        cur.execute("SELECT cities.name\
        FROM cities\
        INNER JOIN states\
        ON cities.state_id = states.id\
        WHERE states.name=%s", (sys.argv[4],))
        rows = cur.fetchall()
        if rows:
            for i in range(0, len(rows)):
                if i == (len(rows) - 1):
                    print(rows[i][0])
                else:
                    print("{}, ".format(rows[i][0]), end='')
        else:
            print()
    except:
        print()
    cur.close()
    conn.close()
