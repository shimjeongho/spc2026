import sqlite3

conn = sqlite3.connect('example.db')
cur = conn.cursor()

# users 테이블의 데이터 개수를 확인
cur.execute('SELECT COUNT(*) FROM users')
count = cur.fetchone()[0]
print(count)

# 데이터가 없을 때만 삽입
if count == 0:
    cur.execute('''
        INSERT INTO users (name, age) VALUES (?, ?)
    ''', ('Alice', 30))

    cur.execute('''
        INSERT INTO users (name, age) VALUES ('Bob', 25)
    ''')

    conn.commit()
else:
    print("이미 테이블에 데이터가 있습니다.")

conn.close()