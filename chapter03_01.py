# 숫자형

# 파이썬 지원 자료형

"""
int : 정수
float : 실수
complex : 복소수
bool : 불린
str : 문자열(시퀀스)
list : 리스트(시퀀스)
tuple : 튜플(시퀀스)
set : 집합
dict : 사전
"""

# 데이터 타입
str1 = "Python"
bool = True
str2 = "Anaconda"
float_v = 10.0 # 10 <> 10.0
int_v = 7
list = [str1, str2]
dict = {
    "name":"Machine Learning",
    "version": 2.0
}
tuple = (7, 8, 9)
set = {7, 8, 9}

# 데이터 타입 출력
print(type(str1))
print(type(bool))
print(type(str2))
print(type(float_v))
print(type(int_v))
print(type(list))
print(type(dict))
print(type(set))
print(type(tuple))

# 숫자형 연산자
"""
+
-
*
/
// : 몫만 계산
% : 나머지
abs : 절댓값
pow(2, 5) = 2의 5제곱
"""

# 정수 선언
i = 77
i2 = -14
big_int = 777777777777777777777777

# 실수 선언
f = 0.9999
f2 = 3.141592
f3 = -3.9
f4 = 3/9

# 연산
i1 = 99
i2 = 9239
big_int1 = 93280484813048250823
big_int2 = 120449493991993991494
f1 = 1.234
f2 = 3.401
i_before = 79200

print("i1+i2 : ", i1+i2)
print(i_before * 4 / 5)

# 형 변환 실습
a = 3.
b = 6
c = .4
d = 12.5

print(type(a), type(b), type(c), type(d))
print()

print(float(b))
print(int(True))
print(complex(3.0)) # complex는 복소수로 변환
print(complex('3.0')) # 문자열도 숫자형으로 바꿔서 계산
print()

# 수치 연산 함수
print(abs(-4))
x, y = divmod(100,9) # 100을 9로 나눈 몫을 x에, 나머지를 y에 넣어라
print(x, y)

# 외부 모듈(패키지 안에 있는)
import math

print(math.pi)
print(math.ceil(5.1)) # x 이상의 수 중에서 가장 작은 정수