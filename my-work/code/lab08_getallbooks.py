import sqlite3 
import os
print("Database path:", os.path.abspath("pfda.db"))

con = sqlite3.connect("pfda.db") 
cur = con.cursor() 
 
for row in cur.execute("select * from book"): 
    print (f"row{row}")