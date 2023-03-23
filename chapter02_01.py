# Print 사용법

# 기본 출력
print('python start')
print('python end')
print('python start')
print('python end')
print()

# separator 옵션
print('P', 'Y', 'T', 'H', 'O', 'N', sep=',')
print('P', 'Y', 'T', 'H', 'O', 'N', sep='')
print('010', '5744', '0511', sep='-')
print('python', 'google.com', sep='@')
print()

# end 옵션 - 다음 프린트문에 이어주기(프린트문을 길게 볼수있게 해주는 법)
print('Welcome to', end=' ')
print('IT News', end=' ')
print('WebSite')
print()

# file 옵션
import sys
print('Learn python', file=sys.stdout)
print()

# format 사용(d:정수, s:문자형, f:3.14242) ---- % 와 format 함수
print('%s %s' % ('one', 'two'))
print('{} {}'.format('one', 2)) # 형식 자동 매칭
print('{1} {0}'.format('one', 'two')) # 뒤에가 one two 여도 앞에 순서가 0이 먼저이기 때문에 two one 으로 출력
print()

# %s
print('%10s' % ('nice')) #10자리 확보하고 왼쪽을 공백으로 해줘 - print('%10s' % ('nice'))
print('{:>10}'.format('nice')) #왼쪽에 10자리를 확보해주고 nice로 포맷해줘 - print('{:>10}.format('nice'))
print('%-10s' % ('nice'))
print('{:<10s}'.format('nice'))
print('{:_>10}'.format('nice')) #왼쪽을 공백으로 채우지말고 _로 채워줘

print('{:^10}'.format('nice')) #중앙정렬

print('%.5s' % ('nice'))
print('%.5s' % ('goodboy')) #다섯글자만 출력
print('{:10.5}'.format('pythonstudy')) #공간은 10개, 그렇지만 쓰는건 5개
print('{:_>10.5}'.format('scottyoon410'))
print()

# %d
print('%d %d' % (1,2))
print('{} {}'.format(1,2))

print('%4d' % (42))
print('{:4d}'.format(42))
print()

# %f - 실수, 소수
print('%f' % (3.1416926273))
print('%1.8f' % (13.1416926273)) #정수는 1자리, 소수는 8자리 나와라
print('{:f}'.format(3.1416926273))
print('%06.2f'.format(3.14169262733121))
print('{:06.2f}'.format(3.14169262733121))
print()

# 연습
""" 
print('%s' % ('Provide'))
print('{}'.format('Provide'))
print('%100s' % 'remember')
print('{:>100s}'.format('remember'))
print('{:^100s}'.format('remember'))
print('{:10.3s}'.format('Firenze'))
print('{:_^10s}'.format('Florence'))
print('{:>20s}'.format('Firenze'))
print() 
"""

print('%d' % 19970410)
print('{:d}'.format(19970410))
print('{}__{}__{}'.format(19970,410,1078))
print('%10d' % 42)
print('{:30d}'.format(50))