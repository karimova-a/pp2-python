import psycopg2
from config import load_config
import csv

#1-connect database
def connect():
    return psycopg2.connect(
        host="localhost",
        database="phonebook",
        user="postgres",
        password="password"       
    )

#2-create table(already created in terminal)
def create_table():
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS phonebook (
                    id SERIAL PRIMARY KEY,
                    first_name VARCHAR(100),
                    phone VARCHAR(20) UNIQUE
                );
            """)
            print("PhoneBook table ready.")

#3-csv import
def insert_from_csv(filename):
    with connect() as conn:
        with conn.cursor() as cur:
            with open(filename, newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    cur.execute("""
                        INSERT INTO phonebook (first_name, phone)
                        VALUES (%s, %s)
                        ON CONFLICT (phone) DO NOTHING;
                    """, (row['first_name'], row['phone']))
            print("Data uploaded from CSV.")

#4-from console
def insert_from_console():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                INSERT INTO phonebook (first_name, phone)
                VALUES (%s, %s)
                ON CONFLICT (phone) DO NOTHING;
            """, (name, phone))
            print("Contact added.")

#5-contact update
def update_contact():
    print("Update (1) name or (2) phone?")
    choice = input("Your choice: ")

    with connect() as conn:
        with conn.cursor() as cur:
            if choice == "1":
                phone = input("Enter phone to update name for: ")
                new_name = input("New name: ")
                cur.execute("UPDATE phonebook SET first_name = %s WHERE phone = %s", (new_name, phone))
            elif choice == "2":
                name = input("Enter name to update phone for: ")
                new_phone = input("New phone: ")
                cur.execute("UPDATE phonebook SET phone = %s WHERE first_name = %s", (new_phone, name))
            print("Contact updated.")

#6-query(select)
def query_contacts():
    print("Search by (1) name, (2) phone, (3) show all")
    choice = input("Your choice: ")

    with connect() as conn:
        with conn.cursor() as cur:
            if choice == "1":
                name = input("Enter name: ")
                cur.execute("SELECT * FROM phonebook WHERE first_name ILIKE %s", (f"%{name}%",))
            elif choice == "2":
                phone = input("Enter phone: ")
                cur.execute("SELECT * FROM phonebook WHERE phone LIKE %s", (f"%{phone}%",))
            else:
                cur.execute("SELECT * FROM phonebook")
            rows = cur.fetchall()
            for row in rows:
                print(row)

#7-delete
def delete_contact():
    print("Delete by (1) name or (2) phone?")
    choice = input("Your choice: ")

    with connect() as conn:
        with conn.cursor() as cur:
            if choice == "1":
                name = input("Enter name to delete: ")
                cur.execute("DELETE FROM phonebook WHERE first_name = %s", (name,))
            elif choice == "2":
                phone = input("Enter phone to delete: ")
                cur.execute("DELETE FROM phonebook WHERE phone = %s", (phone,))
            print("Contact deleted.")

#8-menu
def menu():
    create_table()
    while True:
        print("\n PhoneBook Menu:")
        print("1. Insert from CSV")
        print("2. Insert from Console")
        print("3. Update Contact")
        print("4. Query Contacts")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            insert_from_csv("contacts.csv")
        elif choice == "2":
            insert_from_console()
        elif choice == "3":
            update_contact()
        elif choice == "4":
            query_contacts()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

#
if __name__ == "__main__":
    menu()

