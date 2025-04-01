from flask import Flask, request
import sqlite3
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

def log_action(data):
    conn = sqlite3.connect('activity_logs.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            action TEXT,
            user_id TEXT,
            browser TEXT,
            ip TEXT,
            location TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    cursor.execute('''
        INSERT INTO logs (action, user_id, browser, ip, location)
        VALUES (?, ?, ?, ?, ?)
    ''', (
        data.get('action'),
        data.get('userId'),
        data.get('browser'),
        data.get('ip'),
        data.get('location')
    ))
    conn.commit()
    conn.close()

@app.route('/log', methods=['POST'])
def log_custom():
    data = request.get_json()
    log_action(data)
    return {'message': 'Logged'}, 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
