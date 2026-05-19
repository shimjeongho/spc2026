import sqlite3

# 데이터베이스 연결
conn = sqlite3.connect('example.db')

# 커서라는 객체를 통해서.. 실제 데이터 입출력을 함
cur = conn.cursor()

# 테이블 생성
cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
             name TEXT NOT NULL,
             age INTEGER NOT NULL
    )
""")

conn.commit()  # 변경사항 저장

conn.close()  # 데이터베이스 연결 종료

"""
(base) C:\src\SPC2026\7.PYTHON\18.database>sqlite3 example.db
SQLite version 3.51.2 2026-01-09 17:27:48
Enter ".help" for usage hints.
sqlite> .tables
users
"""