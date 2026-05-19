import database.my_crud_lib as db

def main():
    db.create_table()

    db.insert_user('Alice', 30)
    db.insert_user('Bob', 25)
    db.insert_user('Charlie', 35)

    print('사용자 조회')
    users = db.get_users()
    for user in users:
        print(user)
    
    db.update_user('Alice', 40)
    db.update_user('Bob', 33)

    print('두번째 조회')
    user = db.get_user_by_name('Alice')
    print(user)

    db.delete_user_by_name('Alice')

    print('세번째 조회')
    users = db.get_users()
    for user in users:
        print(user)

if __name__ == '__main__':
    main()

"""
database.my_crud_lib.py 파일로 리팩토링 후 결과:

사용자 조회
(1, 'Alice', 40)
(3, 'Alice', 40)
(4, 'Alice', 40)
(5, 'Bob', 33)
(6, 'Charlie', 35)
(7, 'Alice', 30)
(8, 'Bob', 25)
(9, 'Charlie', 35)
두번째 조회
(1, 'Alice', 40)
세번째 조회
(5, 'Bob', 33)
(6, 'Charlie', 35)
(8, 'Bob', 33)
(9, 'Charlie', 35)
"""