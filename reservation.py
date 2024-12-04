import sqlite3 as sql

class Reservation:
    @staticmethod
    def reservation_room():
        while True:
            guest_id = input("Enter guest ID: ")
            if not guest_id.isdigit():
                print("Invalid guest ID. Please enter a numeric value.")
                continue
            break

        while True:
            room_id = input("Enter room ID: ")
            if not room_id.isdigit():
                print("Invalid room ID. Please enter a numeric value.")
                continue
            break

        check_in_date = input("Enter check-in date: ")
        check_out_date = input("Enter check-out date: ")

        con = sql.connect('hotel.db')
        cur = con.cursor()

        cur.execute('''
            INSERT INTO reservations (guest_id, room_id, check_in_date, check_out_date)
            VALUES (?, ?, ?, ?)
        ''', (guest_id, room_id, check_in_date, check_out_date))

        con.commit()
        con.close()

    @staticmethod
    def select_all_reservations():
        con = sql.connect('hotel.db')
        cur = con.cursor()
        cur.execute('''
            SELECT * FROM reservations
        ''')
        reservations = cur.fetchall()
        for reservation in reservations:
            print(reservation)
        con.close()

    @staticmethod
    def delete_reservation():
        while True:
            reservation_id = input("Enter reservation ID: ")
            if not reservation_id.isdigit():
                print("Invalid reservation ID. Please enter a numeric value.")
                continue
            break

        con = sql.connect('hotel.db')
        cur = con.cursor()
        cur.execute('''
            DELETE FROM reservations WHERE id = ?
        ''', (reservation_id,))
        con.commit()
        con.close()