# db/db_handler.py

import os
import mysql.connector
from mysql.connector import pooling
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# --- Database Connection Pool Setup ---
# This is created only once when the module is imported.
try:
    db_pool = pooling.MySQLConnectionPool(
        pool_name=os.getenv("DB_POOL_NAME"),
        pool_size=int(os.getenv("DB_POOL_SIZE")),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME"),
    )
    print("Database connection pool created successfully.")
except mysql.connector.Error as err:
    print(f"Error creating connection pool: {err}")
    db_pool = None


def execute_sp(sp_name: str, args: tuple = ()):
    if not db_pool:
        print("Database pool is not available.")
        return None

    results = []
    try:
        conn = db_pool.get_connection()
        cursor = conn.cursor(dictionary=True)   # dictionary=True is key it converts the db response tuple to dictionary!
        cursor.callproc(sp_name, args)

        for result in cursor.stored_results():
            rows = result.fetchall()
            if rows:
                results.append(rows)

    except mysql.connector.Error as err:
        print(f"Database Error: {err}")
        return None 
    finally:
        if 'cursor' in locals() and cursor:
            cursor.close()
        if 'conn' in locals() and conn.is_connected():
            conn.close() # This returns the connection to the pool

    return results