def numbers():
    for i in range(1000000):
        yield i

for num in numbers():
    print(num)
    if num >= 5:
        break

"""
0
1
2
3
4
5
"""