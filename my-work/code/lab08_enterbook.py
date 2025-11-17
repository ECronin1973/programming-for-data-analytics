import sqlite3

con = sqlite3.connect("pfda.db")
cur = con.cursor()

# Prompt user for book details
book = {}
book['title'] = input("Please enter book title: ")
book['author'] = input("Please enter book author: ")
book['ISBN'] = input("Please enter book ISBN: ")

# Insert one book safely
sql = "INSERT INTO book VALUES (:title, :author, :ISBN)"
cur.execute(sql, book)

# Commit changes
con.commit()

# Display all books
for row in cur.execute("SELECT * FROM book"):
    print(f"row {row}")

con.close()
