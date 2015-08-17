import sqlite3
conn = sqlite3.connect('school.db')
print 'Database Created/Opened successfully'

conn.execute('''CREATE TABLE STUDENT
       (ID INT PRIMARY KEY     NOT NULL,
       NAME           TEXT    NOT NULL,
       AGE            INT     NOT NULL,
       ADDRESS        CHAR(50),
       STANDARD         REAL);''')
print "Table created successfully"