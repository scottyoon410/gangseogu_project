# 함수
# 복잡한 프로그램을 함수 단위로 본다면 흐름을 풀어나가기 쉬움
# 코드의 재사용
# 코드의 안정성이 좋아짐

# 함수 정의 방법
# def function_name(parameter):
#   code

# 함수의 종류
# 1. 매개변수가 필요한 함수
def function1(x, y):
    print('예제 2 호출', x, y)

function1(1, 2)

# 2. 매개변수가 필요하지 않은 함수
def function2():
    print('예제 1 호출')

function2()

# 3. 결과값을 반환하는 함수(return)
def function3(x, y):
    return x * y
r = function3(50, 50)

print(r)

# 4. 결과값을 반환하지 않는 함수
def function4(a, b):
    print('예제 4 호출', a, b)

function4(1, 2)










# 예제 1
def first_func(w):
    print("Hello,", w)

word = "Kong"

first_func(word)

print()


# 예제 2
def return_func(w):
    value = "Hello, " + str(w)
    return value

x = return_func('GoodGirl')
print(x)

print()


# 예제 3(다중반환)
def func_mul(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return y1, y2, y3

x, y, z = func_mul(10)

print(x, y, z)
print()

# 튜플 리턴
def func_mul2(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return (y1, y2, y3)

q = func_mul2(20)
print(type(q), q, list(q))
print()

# 리스트 리턴
def func_mul3(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return [y1, y2, y3]

p = func_mul3(30)
print(type(p), p, set(p))
print()

# 딕셔너리 리턴
def func_mul4(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return {'v1':y1, 'v2':y2, 'v3':y3}

d = func_mul4(30)

print(type(d), d, d.get('v2'), d.items(), d.keys())

print()


# 중요
# *args, **kwargs

# *args(언패킹)
def args_func(*args):                               # 매개변수의 개수가 동적일 때
    for i, v in enumerate(args):
        print('Result : {}'.format(i), v)
    print('------')

args_func('Yoon')
args_func('Yoon', 'Lee')
args_func('Yoon', 'Lee', 'Kim')

# **kwargs(언패킹)
def kwargs_func(**kwargs):                          # 매개변수의 개수가 동적인데 그게 딕셔너리 형일 때
    for v in kwargs.keys():
        print("{}".format(v), kwargs[v])
    print("------")

kwargs_func(name1 = 'Yoon')
kwargs_func(name1 = 'Yoon', name2 = 'Lee')
kwargs_func(name1 = 'Yoon', name2 = 'Lee', name3 = 'Kim')

# 전체 혼합
def example(args_1, args_2, *args, **kwargs):
    print(args_1, args_2, args, kwargs)

example(10, 20, 'Lee', 'Kim', 'Park', 'Cho', age1 = 10, age2 = 20, age3 = 30)

print()


# 중첩 함수
def nested_func(num):           # 1
    def func_in_func(num):      # 4
        print(num)              # 5
    print("In func")            # 2
    func_in_func(num + 100)     # 3

nested_func(1000)

print()


# 람다식 예제
# 메모리 절약, 가독성 향상, 코드 간결
# 일반적으로 우리가 쓰는 함수는 "객체 생성" -> 메모리 할당
# 람다식은 "즉시 실행 함수"(메모리 초기화)
# 남발 시 가독성 오히려 감소

# def mul_func(x, y):
#     return x * y

# a = lambda x, y: x * y

def mul_func(x, y):
    return x * y

q = mul_func(10, 50)
print(q)

mul_func_var = mul_func
print(mul_func_var(20, 40))

lambda_mul_func = lambda x, y : x * y

print(lambda_mul_func(50, 40))