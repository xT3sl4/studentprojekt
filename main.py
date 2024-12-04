import sqlite3 as sql
from rooms import Rooms
from guests import Guests
from payments import Payments
from reservation import Reservation

class Hotel:
    @staticmethod
    def create_hotel_reservations_db():
        con = sql.connect('hotel.db')
        cur = con.cursor()

        cur.execute('''
            CREATE TABLE IF NOT EXISTS guests (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                phone TEXT NOT NULL
            )
        ''')

        cur.execute('''
            CREATE TABLE IF NOT EXISTS rooms (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                room_number INTEGER NOT NULL,
                type TEXT NOT NULL,
                price REAL NOT NULL
            )
        ''')

        cur.execute('''
            CREATE TABLE IF NOT EXISTS reservations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                guest_id INTEGER NOT NULL,
                room_id INTEGER NOT NULL,
                check_in_date TEXT NOT NULL,
                check_out_date TEXT NOT NULL,
                FOREIGN KEY (guest_id) REFERENCES guests(id),
                FOREIGN KEY (room_id) REFERENCES rooms(id)
            )
        ''')

        cur.execute('''
            CREATE TABLE IF NOT EXISTS payments (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                reservation_id INTEGER NOT NULL,
                amount REAL NOT NULL,
                payment_date TEXT NOT NULL,
                FOREIGN KEY (reservation_id) REFERENCES reservations(id)
            )
        ''')

        con.commit()
        con.close()

def main():
    hotel = Hotel()
    hotel.create_hotel_reservations_db()

    while True:
        print("\nMenu:")
        print("1. Create Room")
        print("2. Select All Rooms")
        print("3. Delete Room")
        print("4. Create Guest")
        print("5. Select All Guests")
        print("6. Delete Guest")
        print("7. Create Reservation")
        print("8. Select All Reservations")
        print("9. Delete Reservation")
        print("10. Create Payment")
        print("11. Select All Payments")
        print("12. Delete Payment")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            Rooms.create_room()
        elif choice == '2':
            Rooms.select_all_rooms()
        elif choice == '3':
            Rooms.delete_room()
        elif choice == '4':
            Guests.create_guest()
        elif choice == '5':
            Guests.select_all_guests()
        elif choice == '6':
            Guests.delete_guest()
        elif choice == '7':
            Reservation.reservation_room()
        elif choice == '8':
            Reservation.select_all_reservations()
        elif choice == '9':
            Reservation.delete_reservation()
        elif choice == '10':
            Payments.create_payment()
        elif choice == '11':
            Payments.select_all_payments()
        elif choice == '12':
            Payments.delete_payment()
        elif choice == '0':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()