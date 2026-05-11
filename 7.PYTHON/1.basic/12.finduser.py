users = [
    {"name": "김민준", "age": 25, "location": "서울", "car": "Hyundai Avante"},
    {"name": "이서연", "age": 34, "location": "부산", "car": "Kia Sorento"},
    {"name": "오지후", "age": 22, "location": "대구", "car": "Tesla Model 3"},
    {"name": "김하은", "age": 31, "location": "인천", "car": "BMW 520d"},
    {"name": "하도윤", "age": 27, "location": "광주", "car": "Genesis G80"},
    {"name": "이예린", "age": 25, "location": "대전", "car": "Kia Ray"},
    {"name": "오시우", "age": 40, "location": "울산", "car": "Mercedes-Benz E-Class"},
    {"name": "김채원", "age": 29, "location": "수원", "car": "Audi A6"},
    {"name": "강현우", "age": 36, "location": "제주", "car": "Hyundai Palisade"},
    {"name": "고유진", "age": 24, "location": "춘천", "car": "Toyota Camry"}
]

def find_user_and_print(name):
    for user in users:
        # if usr["name"] == name:   # 정확한 매칭 찾기
        if user["name"].startswith(name):     # 앞글자, 즉 성씨로 찾기
            print(user)

find_user_and_print("김")
find_user_and_print("오")

def find_user_and_return(name):
    found = [] # 찾을 사용자를 담을 바구니(리스트 변수)

    for user in users:
        if user["name"].startswith(name):
            found.append(user)

    return found

print('-'*30)

# found_users = find_user_and_return("김")
# found_users = find_user_and_return("오")
found_users = find_user_and_return("구")
print("찾은 사용자 : ", found_users)

print('-'*30)

def find_users2(name=None, age=None):
    """이름 또는 나이를 입력받아 매칭되는 사람을 반환한다"""
    found = []

    for user in users:
        if name is not None and age is not None:
            if user["name"] == name and user["age"] == age:
                found.append(user)
        elif name is not None:
            if user["name"] == name:
                found.append(user)
        elif age is not None:
            if user["age"] == age:
                found.append(user)

    return found

print(find_users2("김민준"))
print(find_users2("김민준", 24))
print(find_users2("김민준", 25))
print(find_users2(age=25)) # ??? 나이로만 찾으려면 어떻게

print('-'*30)

# 조금더 좋은 코드
def find_users2_better(name=None, age=None, location=None):
    """이름 또는 나이를 입력받아 매칭되는 사람을 반환한다"""
    found = []
    for user in users:
        #        true     or    비교문
        if (name is None or user["name"] == name) \
            and (age is None or user["age"] == age) \
            and (location is None or user["location"] == location):
            found.append(user)
    return found

print(find_users2_better("김민준", 25, "서울"))
# print(find_users2("김민준", 24))
# print(find_users2("김민준", 25))
# print(find_users2(age=25)) # ??? 나이로만 찾으려면 어떻게


print('-'*30)

search_condition1 = {
    "name": "김민중"
}

search_condition2 = {
    "name": "김민준",
    "age": 25
}
search_condition3 = {
    "age": 25
}

# def find_users2_best(condition):
#     found = []
#     for user in users:
#         if user.get("name") == condition.get("name", "") and \
#             user.get("age") == condition.get('age', 0) and \
#             user.get("location") == condition.get("location", ""):
#             found.append(user)
    
#     return found

# print(find_users2_best(search_condition1))
"""
{'name': '김민준', 'age': 25, 'location': '서울', 'car': 'Hyundai Avante'}
{'name': '김하은', 'age': 31, 'location': '인천', 'car': 'BMW 520d'}
{'name': '김채원', 'age': 29, 'location': '수원', 'car': 'Audi A6'}
{'name': '오지후', 'age': 22, 'location': '대구', 'car': 'Tesla Model 3'}
{'name': '오시우', 'age': 40, 'location': '울산', 'car': 'Mercedes-Benz E-Class'}
------------------------------
찾은 사용자 :  []
------------------------------
[{'name': '김민준', 'age': 25, 'location': '서울', 'car': 'Hyundai Avante'}]
[]
[{'name': '김민준', 'age': 25, 'location': '서울', 'car': 'Hyundai Avante'}]
[{'name': '김민준', 'age': 25, 'location': '서울', 'car': 'Hyundai Avante'}, {'name': '이예린', 'age': 25, 'location': '대전', 'car': 'Kia Ray'}]
------------------------------
[{'name': '김민준', 'age': 25, 'location': '서울', 'car': 'Hyundai Avante'}]
"""