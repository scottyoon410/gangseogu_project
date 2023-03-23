# 반복문
# For 실습

# 코딩의 핵심
# for in <collection>
#   <Loop body>

for v1 in range(10):            # 0~9
    print('v1 is : ', v1)

for v2 in range(1,11):          # 1~10
    print('v2 is : ', v2)

for v3 in range(2, 11, 2):
    print('v3 is : ', v3)

print()

# 1부터 1000까지 합 구하기
sum1 = 0

for v in range(1,1001):
    sum1 += v

print(sum1)

print(sum(range(1,1001)))       #1부터 1000까지의 합
print(sum(range(4,1001,4)))     #1부터 1000까지의 4의 배수의 합


# Iterables 자료형 반복
# 문자열, 리스트, 튜플, 집합, 딕셔너리 사용 가능
# iterable 리턴 함수 : range, reversed, enumerate, filter, map, zip

# 예제 1
names = ['Kim', 'Park', 'Cho', 'Lee', 'Choi', 'Yoon']

for n in names:
    print('You are : ', n)

print()

# 예제 2
lotto_numbers = [24,12,13,19,33,53]

for n in lotto_numbers:
    print('Lotto number is : ', n)

print()

# 예제 3
word = 'Beautiful'

for n in word:
    print("word : ", n)

print()

# 예제 4
my_info = dict(
    name = 'James',
    last_name = 'Lee',
    water_type = 'smooth',
    song = 'hype boy'
)

for n in my_info:
    print(n, "is :", my_info[n])                # for n in my_info: 일때, n은 키값, my_info[n]은 밸류

for v in my_info.values():
    print('values :', v)


# 예제 5
name = 'FineApplE'

for n in name:
    if n.isupper() == True:
        print(n)
    else:
        print(n.upper())

print()


# Break 문
number = [14, 5, 4, 22, 554, 3435, 77, 33, 63, 9, 0]

for n in number:
    if n == 77:
        print('I got it!')
        break
    else:
        print('WTF Where is that?')


# continue 문   -   내가 보기 싫은 값 PASS시킴
lt = ["1", 2, 4, 5, True, complex(3), 5.3]

for v in lt:
    if type(v) is bool:
        continue
    print("current type :", v, type(v))


# for-else 구문  -   끝까지 찾았지만 해당하는 수가 없을 때(break에 해당하는 숫자가 없을 때), else문을 실행
number = [14, 5, 4, 22, 554, 3435, 77, 33, 63, 9, 0]

for num in number:
    if num == 999:
        print("Got it!")
        break
else:
    print("not found")


# 구구단 출력
for n in range(1, 10):
    for m in range(1, 10):
        print('{:4d}'.format(n*m), end=" ")
    print()

print()

# 변환 예제
name2 = 'Aceman'
print(list(reversed(name2)))
print(tuple(reversed(name2)))
print(set(reversed(name2)))         # 순서X