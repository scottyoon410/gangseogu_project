# print 추가설명
# 세가지 print formatting
# 자주 나오는 질문 참고

"""
참고 : Escape 코드

\n : 개행
\t : 탭
\\ : 문자
\' : 문자
\" : 문자
\000 : 널 문자
...

"""

x = 50
y = 100
text = 308276567
n = 'Lee'

# 출력 1
ex1 = 'n = %s, s = %s, sum = %d' % (n, text, (x+y))
print(ex1)

# 출력 2
ex2 = 'n = {n}, s = {s}, sum = {sum}'.format(n = n, s = text, sum = x+y)
print(ex2)

# 출력 3
ex3 = f'n = {n}, s = {text}, sum = {x+y}'
print(ex3)


# 구분기호
m = 100000000
print(f'{m:,}')

print()


# 정렬
# ^ : 가운데 정렬, < : 왼쪽 정렬, > : 오른쪽 정렬

t = 20

print(f't 가운데 정렬: {t:^10}')
print(f't 왼쪽 정렬: {t:<10}')
print(f't 오른쪽 정렬: {t:>10}')

print()
print()

print(f't 가운데 정렬: {t:_^10}')
print(f't 가운데 정렬: {t:*^10}')

