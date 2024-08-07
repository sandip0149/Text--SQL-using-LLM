import sqlite3

connection  = sqlite3.connect("student.db")

## cursor for CRUD

cursor = connection.cursor()

table_info = """
Create table STUDENT(NAME VARCHAR(25) , CLASS VARCHAR(25) , SECTION Varchar(25) ,MARKS INT);
"""

# cursor.execute(table_info)

cursor.execute("INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS) VALUES ('Alice', '10', 'A', 85)")
cursor.execute("INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS) VALUES ('Bob', '10', 'B', 90)")
cursor.execute("INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS) VALUES ('Charlie', '9', 'A', 78)")
cursor.execute("INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS) VALUES ('David', '11', 'C', 92)")
cursor.execute("INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS) VALUES ('Eva', '12', 'B', 88)")


print("Records are")

data = cursor.execute('''Select * From STUDENT''')

# print(data)

for row in data:
    print(row)


connection.commit()

connection.close()