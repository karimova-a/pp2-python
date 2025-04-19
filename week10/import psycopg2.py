import psycopg2

def list_databases():
    # Connect to the default 'postgres' database
    conn = psycopg2.connect(
        dbname="postgres", 
        user="postgres", 
        password="password", 
        host="localhost",
        port="5432"
    )
    conn.autocommit = True  # Required for database-level operations
    cur = conn.cursor()

    # Query to list databases
    cur.execute("SELECT datname FROM pg_database WHERE datistemplate = false;")
    databases = cur.fetchall()

    print("Databases:")
    for db in databases:
        print(f" - {db[0]}")

    cur.close()
    conn.close()

list_databases()
