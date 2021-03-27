#!/usr/bin/python3
"""
Script that lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa.
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
    d_base = sys.argv
    conn = mdb.connect(**args)
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name REGEXP '^N'\
    ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()
