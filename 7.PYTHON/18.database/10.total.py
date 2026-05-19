import sqlite3

# 데이터베이스 연결 유틸
def connect_db():
    conn = sqlite3.connect('example.db')
    cur = conn.cursor()
    return conn, cur

# 데이터베이스 연결 유틸
def disconnect_db(conn):
    conn.commit()
    conn.close()

def create_table():
    conn, cur = connect_db()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL)
        ''')
    disconnect_db(conn)

def insert_user(name, age):
    conn, cur = connect_db()
    cur.execute('''
        INSERT INTO users (name, age) VALUES (?, ?)
    ''', (name, age))
    disconnect_db(conn)

def get_users():
    conn, cur = connect_db()
    cur.execute('SELECT * FROM users')
    users = cur.fetchall() # 모든 결과를 가져옴
    disconnect_db(conn)
    return users

def get_user_by_name(name):
    conn, cur = connect_db()
    cur.execute('SELECT * FROM users WHERE name=?', (name,))
    user = cur.fetchone() # 하나의 결과를 가져옴(동명이인이 있으면 여러명 나올 수 있어서 사실은 fetchall()가 더 안전)
    disconnect_db(conn)
    return user

def update_user(name, age):
    conn, cur = connect_db()
    cur.execute('''
        UPDATE users SET age=? WHERE name=?
    ''', (age, name))
    disconnect_db(conn)

def delete_user_by_name(name):
    conn, cur = connect_db()
    cur.execute('''
        DELETE FROM users WHERE name=?
    ''', (name,))
    disconnect_db(conn)

def delete_user_by_id(id):
    conn, cur = connect_db()
    cur.execute('''
        DELETE FROM users WHERE id=?
    ''', (id,))
    disconnect_db(conn)

def main():
    create_table()

    insert_user('Alice', 30)
    insert_user('Bob', 25)
    insert_user('Charlie', 35)

    print('사용자 조회')
    users = get_users()
    for user in users:
        print(user)

    update_user('Alice', 40)
    update_user('Bob', 33)

    print('두번째 조회')
    user = get_user_by_name('Alice')
    print(user)

    delete_user_by_name('ALice')

    print('세번째 조회')
    users = get_users()
    for user in users:
        print(user)


if __name__ == '__main__':
    main()

"""
사용자 조회
(1, 'Alice', 30)
(3, 'Alice', 30)
(4, 'Alice', 30)
(5, 'Bob', 25)
(6, 'Charlie', 35)
두번째 조회
(1, 'Alice', 40)
세번째 조회
(1, 'Alice', 40)
(3, 'Alice', 40)
(4, 'Alice', 40)
(5, 'Bob', 33)
(6, 'Charlie', 35)
"""