import psycopg2

def connect():
    return psycopg2.connect(
        host="localhost",
        database="phonebook",
        user="postgres",
        password="password" 
    )
def setup_functions_and_procedures():
    with connect() as conn:
        with conn.cursor() as cur:

            # Create table if not exists
            cur.execute("""
                CREATE TABLE IF NOT EXISTS phonebook (
                    id SERIAL PRIMARY KEY,
                    first_name VARCHAR(100),
                    phone VARCHAR(20) UNIQUE
                );
            """)

            # Function: Search by pattern
            cur.execute("""
                CREATE OR REPLACE FUNCTION search_contacts(pattern TEXT)
                RETURNS TABLE(id INT, first_name VARCHAR, phone VARCHAR) AS $$
                BEGIN
                    RETURN QUERY
                    SELECT phonebook.id, phonebook.first_name, phonebook.phone
                    FROM phonebook
                    WHERE phonebook.first_name ILIKE '%' || pattern || '%' 
                       OR phonebook.phone ILIKE '%' || pattern || '%';
                END;
                $$ LANGUAGE plpgsql;
            """)

            # Procedure: Insert or update user
            cur.execute("""
                CREATE OR REPLACE PROCEDURE insert_or_update_user(p_name VARCHAR, p_phone VARCHAR)
                LANGUAGE plpgsql
                AS $$
                BEGIN
                    IF EXISTS (SELECT 1 FROM phonebook WHERE first_name = p_name) THEN
                        UPDATE phonebook SET phone = p_phone WHERE first_name = p_name;
                    ELSE
                        INSERT INTO phonebook(first_name, phone) VALUES (p_name, p_phone);
                    END IF;
                END;
                $$;
            """)

            # Procedure: Insert many users with phone validation
            cur.execute("""
                CREATE OR REPLACE PROCEDURE insert_many_users(
                    IN names TEXT[],
                    IN phones TEXT[],
                    OUT incorrect_data TEXT[]
                )
                LANGUAGE plpgsql
                AS $$
                DECLARE
                    i INT := 1;
                BEGIN
                    incorrect_data := ARRAY[]::TEXT[];

                    WHILE i <= array_length(names, 1) LOOP
                        IF phones[i] ~ '^\\d{6,15}$' THEN
                            CALL insert_or_update_user(names[i], phones[i]);
                        ELSE
                            incorrect_data := array_append(incorrect_data, names[i] || ':' || phones[i]);
                        END IF;
                        i := i + 1;
                    END LOOP;
                END;
                $$;
            """)

            # Function: Pagination
            cur.execute("""
                CREATE OR REPLACE FUNCTION get_contacts(limit_num INT, offset_num INT)
                RETURNS TABLE(id INT, first_name VARCHAR, phone VARCHAR) AS $$
                BEGIN
                    RETURN QUERY
                    SELECT * FROM phonebook ORDER BY id LIMIT limit_num OFFSET offset_num;
                END;
                $$ LANGUAGE plpgsql;
            """)

            # Procedure: Delete by name or phone
            cur.execute("""
                CREATE OR REPLACE PROCEDURE delete_contact(p_name TEXT, p_phone TEXT)
                LANGUAGE plpgsql
                AS $$
                BEGIN
                    DELETE FROM phonebook
                    WHERE (p_name IS NOT NULL AND first_name = p_name)
                       OR (p_phone IS NOT NULL AND phone = p_phone);
                END;
                $$;
            """)

            print("✅ All functions and procedures have been created successfully.")



# Menu-based interaction with procedures/functions
def run():
    while True:
        print("\n PhoneBook SQL Runner")
        print("1. search_contacts(pattern)")
        print("2. insert_or_update_user(name, phone)")
        print("3. insert_many_users(names[], phones[])")
        print("4. get_contacts(limit, offset)")
        print("5. delete_contact(name, phone)")
        print("6. Exit")

        choice = input("Choose a number: ")

        if choice == "1":
            pattern = input("Enter search pattern: ")
            with connect() as conn:
                with conn.cursor() as cur:
                    cur.execute("SELECT * FROM search_contacts(%s)", (pattern,))
                    results = cur.fetchall()
                    for row in results:
                        print(row)

        elif choice == "2":
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            with connect() as conn:
                with conn.cursor() as cur:
                    cur.execute("CALL insert_or_update_user(%s, %s)", (name, phone))
                    print("Procedure executed.")

        elif choice == "3":
            names = input("Enter names (comma-separated): ").split(",")
            phones = input("Enter phones (comma-separated): ").split(",")

            # Trim spaces
            names = [n.strip() for n in names]
            phones = [p.strip() for p in phones]

            with connect() as conn:
                with conn.cursor() as cur:
                    cur.execute("CALL insert_many_users(%s, %s, %s)", (names, phones, []))
                    print("Inserted. (Check DB for invalid data if needed)")

        elif choice == "4":
            limit = int(input("Enter limit: "))
            offset = int(input("Enter offset: "))
            with connect() as conn:
                with conn.cursor() as cur:
                    cur.execute("SELECT * FROM get_contacts(%s, %s)", (limit, offset))
                    results = cur.fetchall()
                    for row in results:
                        print(row)

        elif choice == "5":
            name = input("Enter name (or leave blank): ") or None
            phone = input("Enter phone (or leave blank): ") or None
            with connect() as conn:
                with conn.cursor() as cur:
                    cur.execute("CALL delete_contact(%s, %s)", (name, phone))
                    print("Contact deleted.")

        elif choice == "6":
            print("Exiting.")
            break

        else:
            print("Invalid option.")

if __name__ == "__main__":
    setup_functions_and_procedures()
    run()
