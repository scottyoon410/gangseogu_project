# 파이썬 리스트
# 자료구조에서 중요
# 리스트 자료형 - [순서 있음, 중복 있음, 수정 가능, 삭제 가능]

# 선언
a = []
b = list()
c = [70, 75, 80, 85]
print(len(c))
d = [1000, 10000, 'Ace', 'Base', 'Captine'] # 서로 다른 자료형을 하나의 리스트 안에
e = [1000, 10000, ['Ace', 'Base', 'Captine']]
f = [21.42, 'footbar', 3, 4, False, 3.21342]
print()

# 인덱싱 - 원하는 데이터를 꺼내오는 과정
print(d[1])
print(d[-1])
print(e[-1][1])
print(list(e[-1][1])) # 문자열은 시퀀스니까 Base를 리스트 형태로 만들어서 출력
print()

# 슬라이싱 - 항상 (오른쪽-1) 이라는 거 기억하기
print(d[0:3])
print(d[2:])
print(e[-1][1:3])
print()

# 리스트 연산
# 리스트 + 리스트 = 리스트
print(c+d)
print(d+e)
print(c*3) # 4개의 원소 * 3 but 순서 유지
print('Test :' + str(c[0])) # c[0]이 int이므로 str로 형변환
print()

# 값 비교
print(c == c[:])
print()

# Identity(id)
temp = c
print(temp, c)
print(id(temp))
print(id(c))

# 선언
# a = []
# b = list()
# c = [70, 75, 80, 85]
# print(len(c))
# d = [1000, 10000, 'Ace', 'Base', 'Captine']
# e = [1000, 10000, ['Ace', 'Base', 'Captine']]
# f = [21.42, 'footbar', 3, 4, False, 3.21342]

# 리스트 수정, 삭제
c[0] =4
print(c)
c[1:3] = ['a', 'b', 'c']        # [4, 75, 80, 85] 의 2번째, 3번째를 빼고 a, b, c 를 추가
print(c)
c[1] = ['a', 'b', 'c']
print(c)
c[1:3] = [] 
print(c)
del c[2] # 삭제
print(c)
print()

# 리스트 함수
a = [9,2,6,4,3]
print('a-', a)
a.append(10)
print('a-', a)
a.sort()                             # 오름차순으로 정렬
print('a-', a)
a.reverse()
print('a-', a)
print(a.index(3), a[3])
a.insert(2,7)                        # 세번째 자리에 7을 넣을거야 / 나머지는 뒤로 밀어버리기
print('a-', a)
a.reverse()
print('a-', a)
# del a[6]
# print('a-', a)
a.remove(10)                         # 불필요한 데이터 제거(삭제!!)
print('a-', a)
print(a.pop())                       # 마지막 인덱스 제거
print('a-', a)
print(a.pop())
print('a-', a)
print(a.count(1))                    # 해당 인덱스의 개수 구하기 - 1이 몇개냐?
print('a-', a)
print()

ex = [8, 9]
a.extend(ex)
print('a-', a)

# 반복문 활용
while a:
    data = a.pop()
    print(data)
