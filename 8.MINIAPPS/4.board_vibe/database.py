import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'board.db')

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS posts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            message TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def get_posts():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT id, title, message, datetime(created_at, "localtime") as created_at FROM posts ORDER BY id DESC')
    posts = cursor.fetchall()
    conn.close()
    
    # Convert Row objects to dicts
    return [dict(post) for post in posts]

def add_post(title, message):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO posts (title, message) VALUES (?, ?)', (title, message))
    conn.commit()
    
    post_id = cursor.lastrowid
    cursor.execute('SELECT id, title, message, datetime(created_at, "localtime") as created_at FROM posts WHERE id = ?', (post_id,))
    new_post = cursor.fetchone()
    conn.close()
    
    return dict(new_post) if new_post else None
