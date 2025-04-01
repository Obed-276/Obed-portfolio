import os
from flask import Flask
import sqlite3
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def log_action(action):
    conn = sqlite3.connect('activity_logs.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO logs (action) VALUES (?)', (action,))
    conn.commit()
    conn.close()

@app.route('/')
def home():
    log_action('Visited homepage')
    return 'Activity Logger is live!'

@app.route('/log', methods=['POST'])
def log_custom():
    from flask import request
    data = request.get_json()
    log_action(data.get('action', 'Unknown'))
    return {'message': 'Logged'}, 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
