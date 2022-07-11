import sqlite3

conn = sqlite3.connect('atin.db')
c = conn.cursor()

# command = "insert into information values (1, 'ABC123', 'RED', 'TOYOTA', '100', '2020-01-01')"
command = "select * from information"
# id = "123"
# command = f"DELETE FROM setup_layout WHERE camera_id={id}"
c.execute(command)
conn.commit()
datas = c.fetchall()
for data in datas:
    print(data)
