import sqlite3 as sql

class Payments:
    @staticmethod
    def create_payment():
        while True:
            reservation_id = input("Enter reservation ID: ")
            if not reservation_id.isdigit():
                print("Invalid reservation ID. Please enter a numeric value.")
                continue
            break

        while True:
            amount = input("Enter payment amount: ")
            try:
                amount = float(amount)
                break
            except ValueError:
                print("Invalid amount. Please enter a numeric value.")

        payment_date = input("Enter payment date: ")

        con = sql.connect('hotel.db')
        cur = con.cursor()

        cur.execute('''
            INSERT INTO payments (reservation_id, amount, payment_date)
            VALUES (?, ?, ?)
        ''', (reservation_id, amount, payment_date))

        con.commit()
        con.close()

    @staticmethod
    def select_all_payments():
        con = sql.connect('hotel.db')
        cur = con.cursor()
        cur.execute('''
            SELECT * FROM payments
        ''')
        payments = cur.fetchall()
        for payment in payments:
            print(payment)
        con.close()

    @staticmethod
    def delete_payment():
        while True:
            payment_id = input("Enter payment ID: ")
            if not payment_id.isdigit():
                print("Invalid payment ID. Please enter a numeric value.")
                continue
            break

        con = sql.connect('hotel.db')
        cur = con.cursor()
        cur.execute('''
            DELETE FROM payments WHERE id = ?
        ''', (payment_id,))
        con.commit()
        con.close()