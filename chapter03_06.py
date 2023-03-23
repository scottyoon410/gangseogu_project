# 집합(Set) 특징
# 집합(Set) 자료형 (순서X, 중복X, 수정O, 삭제O)

# 선언
a = set()
print(a)
print(type(a))

b = set([1, 2, 3, 4])
c = set([1, 4, 6, 2])
d = set([1, 3, 'Pet', 'Kong'])
e = {'Doo', 'Cong', 'qux', 'pasta', 'pizza'}
f = {42, (1, 2, 3), 3.1342, 'foo'}

print(b)
print(c)
print(d)
print(e)
print(f)
print()

# 튜플 변환(set -> tuple)
t = tuple(b)
print(t)
print(type(t))
print(t[0], t[2])
print()

# 리스트 변환(set -> list)
l = list(c)
l2 = list(e)
print(l)
print(l2)
print()

# 길이
print(len(a))
print(len(f))

# 활용
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])
print(s1&s2)                        # 교집합 intersection
print(s1.intersection(s2))

print(s1|s2)                        # 합집합 union
print(s1.union(s2))

print(s1-s2)
print(s1.difference(s2))            # 차집합 difference

print()

# 중복 원소 확인
print(s1.isdisjoint(s2))            # 교집합이 있으면 False 반환

# 부분집합 확인
print(s1.issubset(s2))              # s1이 s2의 부분집합이냐
print(s1.issuperset(s2))

print()

# 데이터 추가, 제거
s1 = set([1, 2, 3, 4])

s1.add(5)
print(s1)

s1.remove(5)
print(s1)

s1.discard(6)           #6이 없어도 에러 안남
print(s1)