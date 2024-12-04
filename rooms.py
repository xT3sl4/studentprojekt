import sqlite3 as sql

class Rooms:
    @staticmethod
    def create_room():
        while True:
            room_number = input("Enter room number: ")
            if not room_number.isdigit():
                print("Invalid room number. Please enter a numeric value.")
                continue
            break

        room_type = input("Enter room type: ")

        while True:
            room_price = input("Enter room price: ")
            try:
                room_price = float(room_price)
                break
            except ValueError:
                print("Invalid price. Please enter a numeric value.")

        con = sql.connect('hotel.db')
        cur = con.cursor()

        # Check for duplicate room number
        cur.execute('''
            SELECT COUNT(*) FROM rooms WHERE room_number = ?
        ''', (room_number,))
        if cur.fetchone()[0] > 0:
            print("Room number already exists. Please enter a different room number.")
            con.close()
            return

        cur.execute('''
            INSERT INTO rooms (room_number, type, price)
            VALUES (?, ?, ?)
        ''', (room_number, room_type, room_price))
        con.commit()
        con.close()

    @staticmethod
    def select_all_rooms():
        con = sql.connect('hotel.db')
        cur = con.cursor()
        cur.execute('''
            SELECT * FROM rooms
        ''')
        rooms = cur.fetchall()
        for room in rooms:
            print(room)
        con.close()

    @staticmethod
    def delete_room():
        while True:
            room_id = input("Enter room ID: ")
            if not room_id.isdigit():
                print("Invalid room ID. Please enter a numeric value.")
                continue
            break

        con = sql.connect('hotel.db')
        cur = con.cursor()
        cur.execute('''
            DELETE FROM rooms WHERE id = ?
        ''', (room_id,))
        con.commit()
        con.close()