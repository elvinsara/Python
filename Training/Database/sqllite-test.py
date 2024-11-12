import sqlite3

conn = sqlite3.connect(r"C:\Users\Administrator\Documents\Python Training\Python\Training\Database\Chinook_Sqlite.sqlite")
curr = conn.cursor()
print(curr)
curr.execute("SELECT name from sqlite_master where type='table';")
tables = curr.fetchall()
for table in tables:
    print(table)