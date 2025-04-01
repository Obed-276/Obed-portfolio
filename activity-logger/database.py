import sqlite3

# Connect to SQLite (creates file if it doesn't exist)
conn = sqlite3.connect('activity_logs.db')
cursor = conn.cursor()

# Create logs table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        action TEXT NOT NULL,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
''')

conn.commit()
conn.close()
