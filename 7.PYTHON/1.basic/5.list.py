my_list = [1, 2, 3, 4, 5]

print(my_list)
print(len(my_list))

print(my_list[0]) # 모든 언어의 첫번째 멤버는 0번임
print(my_list[4]) # 4번이 다섯번째 멤버
# print(my_list[5]) # 5번은 없음

print(my_list[-1]) # 리스트의 거꾸로.. (뒤로, 마지막)
print(my_list[-2]) # 뒤에서 두번째.. (잘 쓰이지는 않음)

print(my_list[1:3]) # 슬라이싱 [1] 포함하고 [3] 포함하지 않음
print(my_list[3:5]) # 슬라이싱 [3] 포함하고 [5] 포함하지 않음
print(my_list[:2]) # 시작부터 [2]를 포함하지 않는 것 까지..
print(my_list[2:]) # [2]부터 끝까지..

# 원본 리스트에 멤버 추가하기
my_list.append(6)
print(my_list)

# 특정 위치에 멤버 추가하기
my_list.insert(2, 99) # [2]에 추가
print(my_list)

# 해당 값의 요소 삭제하기
my_list.remove(99) 
print(my_list)

# 특정 인덱스의 요소 삭제하기
my_list.pop(3) # [3] 인덱스 삭제 
print(my_list)

my_list.pop() # 인덱스를 안넣으면 기본적으로 맨 뒤에 값
print(my_list)

my_list.clear() # 리스트 통째로 비우기
print(my_list)

my_list = [5, 2, 1, 3, 4, 7, 6, 8, 9]
print(my_list)

my_list.sort() # 정렬을 하는데, 원본값을 변경하는 함수 sort()
print(my_list)

my_list = [5, 2, 1, 3, 4, 7, 6, 8, 9]
new_list = sorted(my_list) # 원본을 유지하고 복제본을 만듦
print(my_list)
print(new_list)

copyed_list = my_list.copy() # 원본 리스트에 복제본을 만듦
print(copyed_list)
copyed_list.sort(reverse=True)
print(copyed_list)
print(my_list)

# 리스트 컴프리멘션 (어려운데, 쓰면 매우매우 편함)
print('-' * 30)
numbers = [x for x in range(1, 10)]
print(numbers)
numbers = [x for x in range(5)] # 시작 값은 0
print(numbers)
numbers = [x**2 for x in range(5)] # 이전값의 제곱수들이 포함된 리스트
print(numbers)
numbers = [x for x in range(1,10)] # 1부터 9까지 값
print(numbers)
numbers = [x for x in range(1, 10) if x % 2 == 0] # x를 2로 나눈 나머지가 0이면 짝수
print(numbers)
numbers = [x for x in range(1, 10) if x % 2 == 1] # x를 2로 나눈 나머지가 1이면 홀수
print(numbers)
numbers = [x          for x in range(1, 10)          if x % 2 == 1] # 이렇게 띄워서 읽는다
print(numbers)

list1 = [1, 2, 3]
list2 = [4, 5, 6]

list12 = list1 + list2 # 리스트의 합산
print(list12)
print(list1 * 3) # 리스트 자체의 곱 (축 반복)

"""
[1, 2, 3, 4, 5]
5
1
5
5
4
[2, 3]
[4, 5]
[1, 2]
[3, 4, 5]
[1, 2, 3, 4, 5, 6]
[1, 2, 99, 3, 4, 5, 6]
[1, 2, 3, 4, 5, 6]
[1, 2, 3, 5, 6]
[1, 2, 3, 5]
[]
[5, 2, 1, 3, 4, 7, 6, 8, 9]
[1, 2, 3, 4, 5, 6, 7, 8, 9]
[5, 2, 1, 3, 4, 7, 6, 8, 9]
[1, 2, 3, 4, 5, 6, 7, 8, 9]
[5, 2, 1, 3, 4, 7, 6, 8, 9]
[9, 8, 7, 6, 5, 4, 3, 2, 1]
[5, 2, 1, 3, 4, 7, 6, 8, 9]
------------------------------
[1, 2, 3, 4, 5, 6, 7, 8, 9]
[0, 1, 2, 3, 4]
[0, 1, 4, 9, 16]
[1, 2, 3, 4, 5, 6, 7, 8, 9]
[2, 4, 6, 8]
[1, 3, 5, 7, 9]
[1, 3, 5, 7, 9]
[1, 2, 3, 4, 5, 6]
[1, 2, 3, 1, 2, 3, 1, 2, 3]
"""