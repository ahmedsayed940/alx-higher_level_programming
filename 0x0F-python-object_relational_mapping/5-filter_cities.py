#!/usr/bin/python3
"""  takes in the name of a state as an argument and lists all cities """
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    c = db.cursor()
    c.execute("""SELECT cities.name FROM
              cities INNER JOIN states ON states.id=cities.state_id
              WHERE states.name=%s""", (sys.argv[4], ))
    rows = c.fetchall()
    i = list(row[0] for row in rows)
    print(*i, sep=", ")
    c.close()
    db.close()
