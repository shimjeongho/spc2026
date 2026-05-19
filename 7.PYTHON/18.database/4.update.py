import sqlite3

conn = sqlite3.connect('example.db')
cur = conn.cursor()

# SELECT 문을 사용하여 데이터 조회
cur.execute('''
    UPDATE users SET age=? WHERE name=?
''', (33, 'Bob'))

conn.commit()
conn.close()

"""
C:\src\SPC2026\7.PYTHON\18.database>python 3.select.py
(1, 'Alice', 30)
(2, 'Bob', 33)
(3, 'Alice', 30)
(4, 'Bob', 33)
"""