import psycopg2
import datetime

def connect():
    return psycopg2.connect(
        host="localhost",
        database="phonebook",
        user="postgres",
        password="password" 
    )

def create_tables():
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS users_snake (
                    id SERIAL PRIMARY KEY,
                    username VARCHAR(50) UNIQUE
                );
            """)
            cur.execute("""
                CREATE TABLE IF NOT EXISTS user_score (
                    id SERIAL PRIMARY KEY,
                    user_id INTEGER REFERENCES users(id),
                    score INTEGER,
                    level INTEGER,
                    saved_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );
            """)
            print("Tables 'users_snake' and 'user_score' are ready.")

def get_or_create_user(username):
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT id FROM users_snake WHERE username = %s", (username,))
            result = cur.fetchone()
            if result:
                return result[0]
            else:
                cur.execute("INSERT INTO users_snake (username) VALUES (%s) RETURNING id", (username,))
                return cur.fetchone()[0]

def get_user_level(user_id):
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT level FROM user_score 
                WHERE user_id = %s 
                ORDER BY saved_at DESC 
                LIMIT 1
            """, (user_id,))
            result = cur.fetchone()
            return result[0] if result else 1

def save_game(user_id, score, level):
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                INSERT INTO user_score (user_id, score, level, saved_at)
                VALUES (%s, %s, %s, %s)
            """, (user_id, score, level, datetime.datetime.now()))
            print("Game saved!")
