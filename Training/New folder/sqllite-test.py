import sqlite3

conn = sqlite3.connect(r"C:\Users\Administrator\Documents\Python Training\Python\Training\New folder\Chinook_Sqlite.sqlite")
curr = conn.cursor()
print(curr)