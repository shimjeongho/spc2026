from employee import Employee
from person import Person
from driver import Driver

employee1 = Employee("James", 25, "Samsung")
employee2 = Employee("John", 27, "LG")
employee3 = Person("Bob", 30)
employee4 = Driver("홍길동", 40, "BMW")

employee1.greet()
employee2.greet()
employee3.greet()
employee4.greet()

employee3.set_age(40)
employee3.greet()
print(employee3.get_name())
employee4.drive()
employee4.drive_fast()

"""
안녕하세요, 저는 Samsung 에 다니고 있는 James 입니다.
안녕하세요, 저는 LG 에 다니고 있는 John 입니다.
안녕하세요, 저는 30살 Bob 입니다.
안녕하세요, 저는 40살 홍길동 입니다.
안녕하세요, 저는 40살 Bob 입니다.
Bob
홍길동 은 BMW 운전을 시작합니다.
홍길동 은 BMW 과속 운전을 시작합니다.
"""