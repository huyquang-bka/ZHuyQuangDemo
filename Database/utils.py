import sqlite3
from datetime import datetime


class Database():
    def __init__(self):
        self.conn = sqlite3.connect('Database/atin.db', check_same_thread=False)
        self.c = self.conn.cursor()

    def get_plate_list(self):
        self.c.execute("select plate from parking")
        columns = self.c.fetchall()
        plates = [column[0] for column in columns]
        return plates

    def get_color_list(self):
        self.c.execute("select color from parking")
        columns = self.c.fetchall()
        colors = [column[0] for column in columns]
        return colors

    def get_brand_list(self):
        self.c.execute("select brand from parking")
        columns = self.c.fetchall()
        brands = [column[0] for column in columns]
        return brands

    def get_info(self, search_dict):
        result_dict = {}
        plate = search_dict['plate'].strip().upper()
        color = search_dict['color'].strip().upper()
        brand = search_dict['brand'].strip().upper()
        if plate:
            command = f"select * from parking where plate='{plate}'"
        elif color and brand:
            command = f"select * from parking where color='{color}' and brand='{brand}'"
        elif color:
            command = f"select * from parking where color='{color}'"
        elif brand:
            command = f"select * from parking where brand='{brand}'"
        else:
            return result_dict
        self.c.execute(command)
        columns = self.c.fetchall()
        for column in columns:
            id, plate, color, brand, in_time, out_time, img_path = column
            result_dict[id] = {'plate': plate, 'color': color, 'brand': brand, 'in_time': in_time, 'out_time': out_time,
                               'img_path': img_path}
        return result_dict

    def insert_to_db(self, dictionary):
        id = dictionary['id']
        plate = dictionary['plate'].strip().upper()
        color = dictionary['color'].strip().upper()
        brand = dictionary['brand'].strip().upper()
        img_path = dictionary['img_path']
        in_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        out_time = "None"
        command = f"insert into parking values({id}, '{plate}', '{color}', '{brand}', '{in_time}', '{out_time}', '{img_path}')"
        self.c.execute(command)
        self.conn.commit()

    def get_number_of_rows(self):
        self.c.execute("select * from parking")
        rows = self.c.fetchall()
        return len(rows)
