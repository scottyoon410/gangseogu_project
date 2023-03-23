# 파이썬 튜플
# 리스트와 비교
# 튜플 (순서 있음, 중복 가능, 수정 안됨!, 삭제 안됨!) --> 불변
# 중요한 데이터를 한번 저장해서 계속 쓰도록

# 선언
a = ()
b = (1)

print(type(a), type(b))

b = (1,)
print(type(a), type(b))

c = (11, 12, 13, 14)
d = (100, 1000, 'Ace', 'Base', 'Captine')
e = (100, 1000, ('Ace', 'Base', 'Captine'))

# 인덱싱
print(d[0])
print(d[0] + d[1])
print(e[-1])
print(type(e[-1]))
print(e[-1][1])
print(list(e[-1][1]))
print()

# 수정 x
# d[0] = 111

# 슬라이싱
print(d[0:3])
print(d[2:])
print(e[2][1:3])
print()

# 튜플 연산
print(c+d)
print(d+e)
print(c*3)

# 튜플 함수
a = (5, 2, 3, 1, 4)
print(a.index(3))       # 숫자 3이 있는 순서가 어디냐
print(a.count(2))       # 숫자 2의 개수가 몇개냐
print()

# 패킹 & 언패킹 (Packing, Unpacking)
# 패킹
t = ('foo', 'bar', 'bax', 'qux')    # 이거 자체가 패킹

# 언패킹1
(x1, x2, x3, x4) = t                # 묶여있던걸 각각 풀어서 할당
print(type(x1), type(x2), type(x3), type(x4))
print(x1, x2, x3, x4)

# 패킹 & 언패킹
t2 = 1, 2, 3                        # 패킹      () 안해도 튜플로 묶어줌
t3 = 4,                             # 패킹
x1, x2, x3 = t2                     # 언패킹
x4, x5, x6 = 4, 5, 6                # 언패킹

print(t2)
print(type(t2))
print(t3)
print(x1, x2, x3)
print(x4, x5, x6)