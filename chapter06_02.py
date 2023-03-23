# 파이썬 모듈
# module : 함수, 변수, 클래스 등 파이썬 구성 요소 등을 모아놓은 파일

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def power(x, y):
    return x ** y


print('-'*15)
print('called! inner!')
print(add(5, 5))
print(subtract(15, 5))
print(multiply(10, 39))
print(divide(46, 3))
print(power(3, 7))
print('-'*15)

# __name__ 사용
