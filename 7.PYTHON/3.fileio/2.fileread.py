# 1. 작은 파일 열기
with open("file.txt", "r", encoding="utf-8") as file:
    data = file.read()
    print("파일 내용: ", data)

# 2. Legacy 파일 open / read / close 패턴
# file = open("file.txt", "r", encoding="utf-8")
# data = file.read()
# file.close()
# print(data)

# 3. 큰 파일 읽기
with open("file.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

    for line in lines:
        print("파일 내용: ", line)

"""
파일 내용:  한글 테스트 
Hello, World Again 333
파일 내용:  한글 테스트 

파일 내용:  Hello, World Again 333
"""