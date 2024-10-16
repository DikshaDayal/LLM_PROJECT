import sqlite3

# Connecting to sqlite
conn = sqlite3.connect('student.db')

# Creating a cursor object
cursor = conn.cursor()

# Creating table if it does not exist
table = """CREATE TABLE IF NOT EXISTS STUDENT(
    NAME VARCHAR(255),
    CLASS VARCHAR(255),
    SECTION VARCHAR(255),
    MARKS INTEGER
);"""
cursor.execute(table)

# Optionally insert some records if needed
cursor.execute("INSERT INTO STUDENT VALUES ('Diksha', 'COE', 'A', 99)")
cursor.execute("INSERT INTO STUDENT VALUES ('Anish', 'IT', 'A', 82)")
cursor.execute("INSERT INTO STUDENT VALUES ('Garvit', 'COE', 'B', 95)")
cursor.execute("INSERT INTO STUDENT VALUES ('Krish', 'ECE', 'B', 90)")
cursor.execute("INSERT INTO STUDENT VALUES ('Himanshu', 'ECE', 'B', 84)")
cursor.execute("INSERT INTO STUDENT VALUES ('Deepanshu', 'EE', 'A', 78)")
cursor.execute("INSERT INTO STUDENT VALUES ('Anugrah', 'EE', 'A', 65)")
cursor.execute("INSERT INTO STUDENT VALUES ('Rishu Raj', 'COE', 'C', 69)")

# Commit the changes
conn.commit()

# Closing the connection
conn.close()
