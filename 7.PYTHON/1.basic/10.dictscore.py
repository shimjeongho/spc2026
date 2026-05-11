students = {
    "김철수": 87,
    "이영희": 92,
    "박민수": 78,
    "최지은": 95,
    "아이유": 81,
    "홍길동": 89,
    "고길동": 73,
    "박길유": 98,
    "백예린": 84,
    "한지민": 91,
}

print(students)


def get_a_students(students):
    a_students = []
    for name, score in students.items(): # dict의 요소를 하나씩 가져와서(items())
        if score >= 90:
            a_students.append(name)
    return a_students

print("A등급 학생: ", get_a_students(students))

"""
{'김철수': 87, '이영희': 92, '박민수': 78, '최지은': 95, '아이유': 81, '홍길동': 89, '고길동': 73, '박길유': 98, '백예린': 84, '한지민': 91}
A등급 학생:  ['이영희', '최지은', '박길유', '한지민']
"""