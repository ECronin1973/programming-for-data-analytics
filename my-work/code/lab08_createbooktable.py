import sqlite3
import os

db_path = os.path.abspath("pfda.db")
print("Database path:", db_path)

con = sqlite3.connect("pfda.db")  # creates file if not present
cur = con.cursor()

# create table
cur.execute("CREATE TABLE IF NOT EXISTS book(title TEXT, author TEXT, ISBN TEXT)")

# commit changes so they persist
con.commit()

print("Table created successfully")

con.close()
