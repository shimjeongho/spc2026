print('Hello, Python')
print('Hello', 'Python')
print('Hello' + 'Python')
print("Hello, " + 'Python')
print('"Hello", ' + "'Python'" + "!!")
num = 5
name = "홍길동"
print("Hello, {}".format(name));
print("Hello, {}. My lucky number is {}".format(name, num));
print("Hello, {0}. My lucky number is {1}".format(name, num));
print("Hello, {1}. My lucky number is {0}".format(name, num));
print('Hello, %s' % name)
print('Hello, %s' % name, end="") # 줄바꿈 없애기
print("홍길동", end="")
print("홍길동", end="\n")
pi = 3.141592
print(f'{pi:.2f}')
print(f'{10:>5}')
print(f'{10:<5}')
print(f'{10:^5}')
print(f"{7:03}") # 패딩
money = 1000000
print(f"{money:,}")

multiline = """
멀티라인으로
긴 주석을 넣을 수 잇습니다.
 이걸 주석이라고 배웠을텐데 사실은 주석이 아니고 여러줄의 문자열입니다.
Hello, Python
Hello Python
HelloPython
Hello, Python
"Hello", 'Python'!!
Hello, 홍길동
Hello, 홍길동. My lucky number is 5
Hello, 홍길동. My lucky number is 5
Hello, 5. My lucky number is 홍길동
Hello, 홍길동
Hello, 홍길동홍길동홍길동
3.14
   10
10   
 10  
007
1,000,000
"""