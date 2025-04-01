from flask import Flask
import sqlite3

app = Flask(__name__)

def log_action(action):
    conn = sqlite3.connect('activity_logs.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO logs (action) VALUES (?)', (action,))
    conn.commit()
    conn.close()

@app.route('/')
def home():
    log_action('Visited homepage')
    return 'Activity Logger is logging visits!'

if __name__ == '__main__':
    app.run(debug=True)
