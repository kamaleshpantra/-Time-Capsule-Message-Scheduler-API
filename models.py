import sqlite3
from datetime import datetime

# Initialize the SQLite database
def init_db():
    conn = sqlite3.connect("time_capsule.db")
    cursor = conn.cursor()
    # Create the Messages table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            message TEXT NOT NULL,
            delivery_date TEXT NOT NULL,  -- Format: YYYY-MM-DD
            recipient TEXT NOT NULL,
            created_at TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

# Add a new message to the database
def add_message(message, delivery_date, recipient):
    conn = sqlite3.connect("time_capsule.db")
    cursor = conn.cursor()
    created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute("""
        INSERT INTO messages (message, delivery_date, recipient, created_at)
        VALUES (?, ?, ?, ?)
    """, (message, delivery_date, recipient, created_at))
    conn.commit()
    conn.close()

# Get all pending messages (future delivery dates)
def get_pending_messages():
    conn = sqlite3.connect("time_capsule.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM messages WHERE delivery_date > date('now')")
    messages = cursor.fetchall()
    conn.close()
    return messages

# Get messages due today
def get_messages_due_today():
    conn = sqlite3.connect("time_capsule.db")
    cursor = conn.cursor()
    today = datetime.now().strftime("%Y-%m-%d")
    cursor.execute("SELECT * FROM messages WHERE delivery_date = ?", (today,))
    messages = cursor.fetchall()
    conn.close()
    return messages