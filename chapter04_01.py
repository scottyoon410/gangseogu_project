# 파이썬 제어문
# IF 실습

# 기본 형식
print(type(True))   # 0이 아닌 수, "abc", [1, 2, 3], (1, 2, 3) ...
print(type(False))  # 0, "", [], {}, () ...

# ex1

if True:
    print('Good')

if False:
    print('Bad')


# ex2

if False:
    print('Bad')
else:
    print('Good')


# 관계 연산자
# > >= < <= == !=

x = 15
y = 10

print(x == y)
print(x != y)

city = ""
if city:
    print("You are in: ", city)
else:
    print("Plz enter your city")

city2 = "Seoul"
if city2:
    print("You are in : ", city2)
else:
    print("Plze enter your city")

print()

# 논리 연산자
# and, or, not

a = 75
b = 40
c = 10

print(a>b and b>c)          # a>b>c
print(a>b or b>c)
print(not a>b)
print(not b>c)
print(not True)
print(not False)

print()

# 산술, 관계, 논리 우선순위
print(3+12 > 7+3)
print(5+10>3 and 7+3 == 10)


# 중첩 ,if else
score1 = 90
score2 = 'A'

if score1 >= 90 and score2 == 'A':
    print('Pass')
else:
    print('Fail')

id1 = 'VIP'
id2 = 'admin'
grade = 'Platinum'

if id1 == 'vip' or id2 == 'admin':
    print('관리자 입장')

if id2 == 'admin' and grade == 'Platinum':
    print('최상위 관리자')

# 다중 조건문
num = 32

if num >= 90:
    print('Grade : A')
elif num >=80:
    print('Grade : B')
elif num >=75:
    print('Grade : C')
else:
    print('과락')

# 중첩 조건문
grade = 'A'
total = 80

if grade == 'A':
    if total >= 90:
        print('장학금 100%')
    elif total >= 80:
        print('장학금 80%')
    elif total >= 70:
        print('장학금 50%')
else:
    print('장학금 없음')


# in, not in 
q = [10, 30, 50]
w = {70, 80, 90, 100}
e = {'Name': 'Lee', 'City': 'Seoul', 'grade': 'A'}
r = (10,30,300)
