
# 우리가 하고싶은것: 서버에서 바뀌는 데이터를 알아서 반환한다.
# 아래처럼 함수르 부르면 1을 줬다가, 2가 됐으면 2를 주고 3이면 3을 주고

# def test():
#     return 1
#     return 2
#     return 3

# x = test()
# print(x)
"""
1
"""

def test():
    print("A")  # 이 함수가 수행할 다양한 일
    yield 1     # 여기에서 일단 멈춤 (return 1)

    print("B")  # 이 함수가 수행할 그 다음 다양한 일들
    yield 2     # 여기에서 일단 멈춤 (return 2)

    print("C")
    yield 3

"""
A
1
B
2
C
3
"""
x = test() # generator 라는 것이 만들어짐 - 동적으로 바뀌는 데이터를 전달하는 객체

# print(x)
print(next(x))
print(next(x))
print(next(x))
# print(next(x))

try:
    while True:
        print(next(x))

except StopIteration:
    print("모든 데이터 사용 완료")