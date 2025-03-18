import sqlite3

## connect to sqlite 
connection = sqlite3.connect('student.db')

## create the cursor object 
cursor = connection.cursor()

## create the table 
table_info = """
CREATE TABLE IF NOT EXISTS STUDENT (
    NAME VARCHAR(25), 
    CLASS VARCHAR(25), 
    SECTION VARCHAR(25), 
    MARKS INT
);
"""
cursor.execute(table_info)

## insert some more records 
students = [
    ('Krish', 'Data Science', 'A', 90),
    ('John', 'Machine Learning', 'B', 85),
    ('Emma', 'Artificial Intelligence', 'A', 95),
    ('Liam', 'Deep Learning', 'C', 75),
    ('Sophia', 'Big Data', 'B', 88),
    ('Aiden', 'Computer Vision', 'A', 92),
    ('Olivia', 'NLP', 'B', 87),
    ('Noah', 'Cybersecurity', 'C', 80)
]

#cursor.executemany("INSERT INTO STUDENT VALUES (?, ?, ?, ?)", students)

## Display all the records 

print("The inserted records are ")
data = cursor.execute("SELECT * FROM STUDENT")

for row in data:
    print(row)

## Commit and close the connection
connection.commit()
connection.close()
