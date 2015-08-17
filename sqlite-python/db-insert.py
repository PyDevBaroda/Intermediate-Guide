#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('school.db')
print "Opened database successfully";

conn.execute("INSERT INTO STUDENT (ID,NAME,AGE,ADDRESS,STANDARD) \
      VALUES (1, 'Harsh', 22, 'Vadodara', 12 )");

conn.execute("INSERT INTO STUDENT (ID,NAME,AGE,ADDRESS,STANDARD) \
      VALUES (2, 'Manoranjan', 22, 'Ahmedabad', 11 )");

conn.commit()
print "Records created successfully"
conn.close()