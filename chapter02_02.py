# 파이썬 변수

# 기본 선언
n = 700
print(n)
print(type(n))

var = 'incruter'
print(var)
print(type(var))

print()

# 동시 선언
x = y = z = 700
print(x, y, z)

# Object Reference
# 변수의 값 할당 상태일 때
# 1. 타입에 맞는 오브젝트 생성 
# 2. 값 생성
# 3. 콘솔 출력

# ex1
print(300)
print(int(300))
print(type(300))

# ex2
n = 777 # 'int'라는 클래스 생성
print(n, type(n))
m = n
print(m, type(m), n, type(n))

m = 400 #재할당
print(m, type(m), n, type(n))

# id(identity) 확인 --> 객체의 고유값 확인 (같은거를 여러개 선언 시 하나가지고 다 공유하고 있다)
m = 800
n = 600
print(id(m))
print(id(n))
print(id(m)==id(n))

# 같은 오브젝트 참조 - 
m = 800
n = 800
print(id(m))
print(id(n))
print(id(m)==id(n)) # 어차피 똑같은거 쓸건데 왜그래~ 하나의 오브젝트로 줄게
print()

# 다양한 변수 선언 방법
# Camel Case : numberOfCollegeGraduates - 처음에는 소문자, 그다음 대문자, 그다음 대문자 -> 메소드 선언시
# Pascal Case : NumberOfCollegeGraduates - 처음부터 대문자, 그다음 대문자, 그다음 대문자 -> 클래스 선언시
# Snake Case : number_of_college_graduates - 모두 소문자, 그 사이는 _ 로 이어줌 -> 변수 선언시

# 허용하는 변수 선언 방법 - 특수문자로 시작 시 '_' or '$' 로 시작
age = 1
Age = 1
AGE = 1
A_g_e = 1
_age = 1
age_ = 1
_AGE_ = 1

# 예약어는 변수명으로 불가능 - for, as, class, break, global, lambda