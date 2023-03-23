# 파이썬 클래스
# 객체지향 프로그래밍 OOP
# self, 인스턴스 메소드, 인스턴스 변수

# 클래스와 인스턴스 차이 이해
# 네임스페이스 : 객체를 인스턴스화 할 때 저장된 공간
# 클래스 변수 : 직접 접근 가능                # 공유할 수 있음
# 인스턴스 변수 : 객체마다 별도 존재

# 예제 1
class Dog2:                              # 모든 클래스는 object를 상속받음 / 여기서는 Dog라는 클래스(틀)를 생성
    # 클래스 속성
    species = 'firstdog'                # 클래스 변수는 species

    # 초기화/인스턴스 속성
    def __init__(self, name, age):      # 클래스가 초기화될 때 반드시 생성되는 함수
        self.name = name                # self가 붙은 것들은 인스턴스 변수
        self.age = age

# 클래스 정보
print(Dog2)

# 인스턴스화
a = Dog2('Dookong', 4)
b = Dog2('Bang_gu', 2)

# 비교
print(a == b, id(a), id(b))

# 네임스페이스
print('dog1', a.__dict__)
print('dog1', b.__dict__)

# 인스턴스 속성 확인
print('{} is {} and {} is {}'.format(a.name, a.age, b.name, b.age))

if a.species == 'firstdog':
    print('{0} is a {1}'.format(a.name, a.species))

print(Dog2.species)
print(a.species)
print(b.species)

print()

# 예제 2
# self 의 이해
class SelfTest:
    def func1():                        # 1) func1 은 클래스 메소드이기 때문에
        print('Func1 called')
    def func2(self):                    # 3) self 가 붙었으니까 func2 는 인스턴스 메소드
        print('Func2 called')

f = SelfTest()

# print(dir(f))
print(id(f))

# f.func1() # 예외
f.func2()                               # 4-1) 인스턴스로 호출하던가

SelfTest.func1()                        # 2) 클래스로 직접 호출(매개변수가 없기 때문에)
SelfTest.func2(f)                       # 4-2) 인스턴스를 넘겨줘야 한다

print()


# 예제 3
# 클래스 변수, 인스턴스 변수
class Warehouse:
    # 클래스 변수
    stock_num = 0   # 재고

    def __init__(self, name):           # 초기화될 때
        self.name = name
        Warehouse.stock_num += 1
    
    def __del__(self):                  # 소멸할 때
        Warehouse.stock_num -= 1

user1 = Warehouse('Lee')                # 인스턴스화
user2 = Warehouse('Cho')

print(Warehouse.stock_num)

print(user1.name)
print(user2.name)
print(user1.__dict__)
print(user2.__dict__)
print('Before', Warehouse.__dict__)

del user1
print('After', Warehouse.__dict__)

print()



class Dog:                              # 모든 클래스는 object를 상속받음 / 여기서는 Dog라는 클래스(틀)를 생성
    # 클래스 속성
    species = 'firstdog'                # 클래스 변수는 species

    # 초기화/인스턴스 속성
    def __init__(self, name, age):      # 클래스가 초기화될 때 반드시 생성되는 함수
        self.name = name                # self가 붙은 것들은 인스턴스 변수
        self.age = age
    
    def info(self):
        return '{} is {} years old'.format(self.name, self.age)
    
    def speak(self, sound):
        return "{} says {}!".format(self.name, sound)


# 인스턴스 생성
c = Dog('July', 4)
d = Dog('Mary', 10)

# 메소드 호출
print(c.info())

# 메소드 호출
print(c.speak('Wall Wall'))
print(d.speak('Mung Mung'))