# backend/wait_for_db.py
import time
import psycopg2
import os

DB_CONFIG = {
    'host': os.getenv('DB_HOST', 'db'),
    'database': os.getenv('DB_NAME', 'logs_db'),
    'user': os.getenv('DB_USER', 'logs_user'),
    'password': os.getenv('DB_PASSWORD', 'logs_password'),
    'port': os.getenv('DB_PORT', 5432)
}

def wait_for_db():
    print("⏳ Waiting for PostgreSQL to be ready...")
    while True:
        try:
            conn = psycopg2.connect(**DB_CONFIG)
            conn.close()
            print("✅ PostgreSQL is ready!")
            break
        except Exception as e:
            print(f"⏳ Retrying in 2s... ({e})")
            time.sleep(2)

if __name__ == "__main__":
    wait_for_db()