import sqlite3

conn = sqlite3.connect('example.db')
cur = conn.cursor()

# SELECT 문을 사용하여 데이터 조회
cur.execute('''
    DELETE FROM users WHERE name=?
''', ('Bob',))

conn.commit()
conn.close()

"""
(1, 'Alice', 30)
(3, 'Alice', 30)
"""