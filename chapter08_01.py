# 파이썬 내장함수 (Built-in)
# 사용하다보면 자연스럽게 숙달
# str(), int(), tuple() 형변환 이미 학습

# 절댓값
# abs()
print(abs(-3))


# all : iterable 요소를 검사 - 모두 참이어야 참
print(all([1,2,3]))
print(all([1,2,0]))
print(all(["",1,2]))


# any : 하나라도 참이면 참
print(any([1,2,3]))
print(any([1,2,0]))
print(any(["",1,2]))


# chr : 아스키 -> 문자로
# ord : 문자 -> 아스키
print(chr(67))
print(ord('C'))


# enumerate : 인덱스 + Iterable 객체 생성
for i, name in enumerate(['abc', 'bcd', 'efg']):
    print(i+1, name)


# filter : 반복 가능한 객체 요소를 지정한 함수 조건에 맞는 값 추출 / 전처리 때 많이 사용
def conv_pos(x):
    return abs(x) > 2

print(list(filter(conv_pos, [1, -3, 2, 0, -5, 6])))
print(list(filter(lambda x: abs(x)>2, [1, -3, 2, 0, -5, 6])))


# id : 객체의 주소값(레퍼런스) 반환
print(id(int(5)))
print(id(int(4)))


# len : 요소의 길이 반환


# max, min : 최댓값, 최솟값
print(max([1, 2, 3]))
print(max('python study'))
print(min([1, 2, 3]))
print(min('pythonstudy'))


# map : 반복가능한 객체 요소를 지정한 함수 실행 후 추출  -  필터는 걸러주지만 그대로 나오게 함 / 전처리 때 많이 사용
def conv_abs(x):
    return abs(x)

print(list(map(conv_abs, [1, -3, 2, 0, -5, 6])))
print(list(map(lambda x: abs(x), [1, -3, 2, 0, -5, 6])))


# pow : 제곱값 반환


# range : 반복가능한 객체 반환
print(range(1, 10, 2))
print(list(range(1, 10, 2)))


# round : 반올림 함수
print(round(6.32132, 2))
print(round(5.6))


# sorted : 반복가능한 객체(Iterable)를 정렬 후 반환
print(sorted([6, 7, 2, 4, 1, 32]))
print(sorted(['p', 'y', 't', 'h', 'o', 'n']))


# sum : 반복가능한 객체(Iterable) 합 반환
print(sum([6, 4, 2, 5, 10]))
print(sum(range(1, 101)))


# type
print(type({'key':'value'}))
print(type({'dict'}))
print(type(()))
print(type([]))


# zip : 반복 가능한 객체(Iterable)의 요소를 묶어서 반환
print(list(zip([10, 20, 30], [40, 50, 60, 70, 80])))
print(type(list(zip([10, 20, 30], [40, 50, 60, 70, 80]))[0]))