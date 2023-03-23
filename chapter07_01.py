# 파이썬 예외 처리의 이해
# 의도한대로 발생하지 않은 것을 처리
# 예외 처리 패턴

# SyntaxError, TypeError, NameError, IndexError, ValueError, KeyError...
# 문법적으로는 예외가 없지만, 코드 실행 단계에서 발생하는 예외도 중요

# 1. 예외는 반드시 처리해야 한다
# 2. 로그는 반드시 남긴다(어떤 예외가 발생했는지 남겨야 함)
# 3. 예외는 던져진다(처리 위임)
# 4. 예외 무시


# SyntaxError : 문법 오류
# print('error)
# if True
#     pass

# NameError : 참조 없음

# KeyError 
dic = {'name':'Lee', 'Age':41, 'City':'Busan'}
# print(dic['hobby'])
print(dic.get('hobby'))

# 예외가 없는 것을 가정하고 프로그램을 작성해라. 런타임 예외 발생 시 예외 처리 권장

# AttributeError : 모듈, 클래스에 있는 잘못된 속성 사용 예외
import time
# print(time.time2())

# FileNotFoundError
# f = open('test.txt')

# TypeError : 자료형에 맞지 않는 연산을 수행 할 경우
x = [1, 2]
y = (2, 3)
# print(x+y)


# 예외 처리 기본
# 1. try : 에러가 발생 할 가능성이 있는 코드 실행
# 2. except 에러명1 : 여러개 가능
# except 에러명2 : 
# else : try 블록의 에러가 없을 경우 실행
# 3. finally : 항상 실행

name = ['Kim', 'Lee', 'Park']

# 예제 1
# try:                    # 외부에 있는 커넥션을 연결할 때
#     z = 'Kim'           # 'Cho'
#     x = name.index(z)
#     print('{}Found it! {} in name'.format(z, x+1))
# except ValueError:
#     print('Not found it! - Occured ValueError!')
# else:
#     print('Ok! else')

print()

print('Pass')

print()

# 예제 2

# try:                    # 외부에 있는 커넥션을 연결할 때
#     z = 'Cho'           # 'Cho'
#     x = name.index(z)
#     print('{}Found it! {} in name'.format(z, x+1))
# except:
#     print('Not found it! - Occured Error!')
# else:
#     print('Ok! else')

print()


# 예제 3
# try:                    # 외부에 있는 커넥션을 연결할 때
#     z = 'Cho'           # 'Cho'
#     x = name.index(z)
#     print('{}Found it! {} in name'.format(z, x+1))
# except Exception as e:
#     print(e)
#     print('Not found it! - Occured Error!')
# else:
#     print('Ok! else')
# finally:
#     print('Ok! finally!')


# 예제 4
# 예외 발생 : raise
# raise 키워드로 예외 직접 발생

# try:
#     a = 'Park'
#     if a == 'Kim':
#         print('Ok! Pass!')
#     else:
#         raise ValueError
# except ValueError:
#     print('Occured! Exception!')
# else:
#     print('Ok! Else!')
# finally:
#     print('Ok! Finally!')