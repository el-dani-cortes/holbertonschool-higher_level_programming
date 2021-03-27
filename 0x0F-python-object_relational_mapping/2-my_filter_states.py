#!/usr/bin/python3
"""
Script that takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument.
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
        "charset": "utf8",
        }
    conn = mdb.connect(**args)
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name='{}' ORDER BY id"
                .format(sys.argv[4]))
    rows = cur.fetchall()
    for row in rows:
        if row[1] == sys.argv[4]:
            print(row)
    cur.close()
    conn.close()
