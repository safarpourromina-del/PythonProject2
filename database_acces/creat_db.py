# create_db.py
import sqlite3


con = sqlite3.connect("products.db")
cur = con.cursor()


cur.execute("CREATE TABLE IF NOT EXISTS products (id INTEGER PRIMARY KEY AUTOINCREMENT, product_name TEXT, product_status TEXT, delivered_at TEXT)")

con.commit()
con.close()

print("Database and table created: products.db / products")