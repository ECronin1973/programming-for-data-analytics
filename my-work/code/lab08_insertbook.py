import sqlite3
import os

db_path = os.path.abspath("pfda.db")
print("Database path:", db_path)

con = sqlite3.connect(db_path)
cur = con.cursor()

# Ensure the table exists with a primary key on ISBN
cur.execute("""
    CREATE TABLE IF NOT EXISTS book (
        title TEXT,
        author TEXT,
        ISBN TEXT PRIMARY KEY
    )
""")

# Check current contents
result = cur.execute("SELECT * FROM book")
print("Before insert:", result.fetchall())

# Insert books safely, ignoring duplicates
books = [
    ("Harry Pothead", "Just Kidding Really", "112344"),
    ("Harry Potter does something profound", "JK Rowling", "123444")
]
cur.executemany("INSERT OR IGNORE INTO book VALUES (?, ?, ?)", books)

# Commit the transaction so data persists
con.commit()

# Check again
result = cur.execute("SELECT * FROM book")
print("After insert:", result.fetchall())

con.close()
