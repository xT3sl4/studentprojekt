import sqlite3 as sql

class Guests:
    @staticmethod
    def create_guest():
        name = input("Enter guest name: ")
        email = input("Enter guest email: ")
        phone = input("Enter guest phone: ")

        if not name or not email or not phone:
            print("All fields are required.")
            return

        con = sql.connect('hotel.db')
        cur = con.cursor()

        cur.execute('''
            INSERT INTO guests (name, email, phone)
            VALUES (?, ?, ?)
        ''', (name, email, phone))

        con.commit()
        con.close()

    @staticmethod
    def select_all_guests():
        con = sql.connect('hotel.db')
        cur = con.cursor()
        cur.execute('''
            SELECT * FROM guests
        ''')
        guests = cur.fetchall()
        for guest in guests:
            print(guest)
        con.close()

    @staticmethod
    def delete_guest():
        while True:
            guest_id = input("Enter guest ID: ")
            if not guest_id.isdigit():
                print("Invalid guest ID. Please enter a numeric value.")
                continue
            break

        con = sql.connect('hotel.db')
        cur = con.cursor()
        cur.execute('''
            DELETE FROM guests WHERE id = ?
        ''', (guest_id,))
        con.commit()
        con.close()