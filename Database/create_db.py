import sqlite3

conn = sqlite3.connect('atin.db')
c = conn.cursor()

c.execute("DROP TABLE IF EXISTS information")
c.execute(
    """CREATE TABLE information (id_car INT, plate TEXT, color TEXT, brand TEXT, speed TEXT, date TEXT)""")

# c.execute("INSERT INTO parking VALUES (1, 'ABC123', 'RED', 'TOYOTA', '2020-01-01', '2020-01-01', 'image/path')")

# conn.commit()

# get all columns name of table
c.execute("PRAGMA table_info(information)")
columns = c.fetchall()
print(columns)
#
# c.execute("SELECT * FROM parking")
# rows = c.fetchall()
# print(rows)
