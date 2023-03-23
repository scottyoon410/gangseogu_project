# 파이썬 딕셔너리
# 범용적으로 가장 많이 사용
# 딕셔너리 자료형(순서X, 키 중복X, 수정O, 삭제O)

# 선언
a = {'name': 'Kim', 'phone': '01057440511', 'nation': "napoli"}             # Key : Value
b = {0: 'first'}
c = {'serie': [1, 2, 3, 4]}
d = {
    'Name': 'Minjae',
    'City': 'Italy',
    'Age': 26,
    'Grade': 'A',
    'Status': True
}

e = dict([
    ('Name', 'Minjae'),
    ('City', 'Florence'),
    ('Age', 26)
])

f = dict(
    Name = 'Minjae',
    city = 'Seoul',
    Age = 24,
    Grade = 'A',
    Status = True
)

# a = [f1, f2, f3...]               -> 딕셔너리를 리스트로 저장하면 차곡차곡, 효율적인 자료구조


print(type(a), a)
print(type(b), b)
print(type(c), c)
print(type(d), d)
print(type(e), e)
print(type(f), f)
print()


# 출력
print(a['name'])
print(a.get('name'))                  # 변수.get('key')

# print(a['name1'])                   # 존재하지 않으면 에러 발생
print(a.get('name1'))                 # 존재하지 않으면 None 처리
print(b[0])
print(b.get(0))

print(f.get('city'))
print(f.get('Age'))
print()


# a = {'name': 'Kim', 'phone': '01057440511', 'nation': "napoli"}             # Key : Value
# b = {0: 'first'}
# c = {'serie': [1, 2, 3, 4]}


# 딕셔너리 추가
a['address'] = 'Seoul'
print(a)
a['rank'] = [1, 2, 3]
print(a)
print(len(a))
print()

# dict_keys, dict_value, dict_items : 반복문(__iter__)에서 사용 가능
# keys()
print(a.keys())
print(b.keys())
print(c.keys())
print(d.keys())

print(list(a.keys()))
print(list(b.keys()))

print()

# values()
print(a.values())
print(b.values())
print(c.values())

print(list(a.values()))
print(list(b.values()))

print()

# items()
print(a.items())
print(b.items())
print(list(a.items()))
print(list(b.items()))

print(type(a.items()))

print()

print(a.pop('name'))
print(a)

print()

print(a.popitem())
print(a)
print(a.popitem())
print(a)
print(a.popitem())
print(a)
print(a.popitem())
print(a)

print()

print('birth' in b)