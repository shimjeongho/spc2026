import sqlite3

conn = sqlite3.connect('example.db')
cur = conn.cursor()

# SELECT 문을 사용하여 데이터 조회
cur.execute('SELECT * FROM users')

# fetchall()는 모든 결과를 리스트로 반환
rows = cur.fetchall()
for row in rows:
    print(row)

conn.close()

"""
2.insert.py 2번 실행 후 결과:

(1, 'Alice', 30)
(2, 'Bob', 25)
(3, 'Alice', 30)
(4, 'Bob', 25)
"""