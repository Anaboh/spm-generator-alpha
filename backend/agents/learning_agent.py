import sqlite3

def track_interaction(user_id, action):
    conn = sqlite3.connect('interactions.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS interactions
                 (id INTEGER PRIMARY KEY, user_id TEXT, action TEXT, timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)''')
    c.execute("INSERT INTO interactions (user_id, action) VALUES (?, ?)", (user_id, action))
    conn.commit()
    conn.close()
