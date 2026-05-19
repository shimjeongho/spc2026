import sqlite3

# 데이터베이스 연결
conn = sqlite3.connect('example.db')

# 커서 생성
cur = conn.cursor()

cur.execute("""
    INSERT INTO users (name, age) VALUES (?, ?)
""", ('Alice', 30))

cur.execute("""
    INSERT INTO users (name, age) VALUES ('Bob', 25)
""")

conn.commit()  # 변경사항 저장
conn.close()  # 데이터베이스 연결 종료


"""
sqlite> SELECT * FROM users;
1|Alice|30
2|Bob|25
"""
