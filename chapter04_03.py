# 파이썬 반복문
# While 실습

# while <expr>:
#   <statement(s)>
# 조건이 만족하는동안 계속 반복, 만족하지 않으면 빠져나감

n = 5
while n > 0:
    n = n-1
    print(n)


# 예제 2
a = ['foo', 'bar', 'baz']

while a:
    print(a.pop())

print()

# 예제 3
# break, continue
n = 5
while n > 0:
    n -= 1
    if n == 2:
        break
    print(n)
print('Loop ended')

print()

# 예제 4
m = 5
while m > 0:
    m -= 1
    if m == 2:
        continue
    print(m)
print('Loop ended')

print()

# 예제 5
i = 1

while i <= 10:
    print(i)
    if i == 6:
        break
    i += 1

print()

# While else 구문
# 예제 6
n = 10
while n >0:
    n -= 1
    print(n)
    if n == 11:
        break
else:
    print('else out.')

print()

# 예제 7
a = ['foo', 'bar', 'baz', 'qux']                    # 리스트 처음부터 돌게 만들고 baz 를 찾게 만드려면
s = 'kim'                                           # i를 0으로 두고, len(a)까지 돌게 한 다음에
i = 0                                               # a[i] 가 baz 일때 break하게 하고
                                                    # 만약 없을때를 대비해서 else: print(~~)
while i < len(a):
    if a[i] == s:
        break
    i += 1
else:
    print(s, 'not fount in list')

print()

# 무한반복 조심
# while True:
#     print('Foo')

a = ['foo', 'bar', 'baz']

while True:
    if not a:               # False이면
        break
    print(a.pop())