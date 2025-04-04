import sqlite3
from config import DB_FILE

def get_db_connection():
    return sqlite3.connect(DB_FILE, check_same_thread=False)

def initialize_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS rp_commands (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        command TEXT UNIQUE NOT NULL,
        description TEXT NOT NULL,
        template TEXT NOT NULL
    )
    """)
    conn.commit()
    conn.close()
