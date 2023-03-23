# 파일 읽기 및 쓰기

# 읽기 모드 : r
# 쓰기 모드 : w
# 추가 모드 : a
# 텍스트 모드 : t
# 바이너리 모드 : b

# 상대 경로 ('../' : 상위 폴더로 이동, './' : 현재 경로)
# 절대 경로 ('/Users/seokyoon/Desktop/python_basic')

# 파일 읽기
# 예제 1

# f = open('/Users/seokyoon/Desktop/python_basic/resource/it_news.txt')
f = open('./resource/it_news.txt', 'r', encoding='UTF-8')

# 속성 확인
print(dir(f))

# 인코딩 확인
print(f.encoding)

# 파일 이름
print(f.name)

# 모드 확인
print(f.mode)

cts = f.read()
print(cts)

f.close()

print()
print()

# 예제 2  -  with 문을 사용해서 as 를 주고 쉽게 사용한다
with open('./resource/it_news.txt', 'r', encoding='UTF-8') as f:
    c = f.read()
    print(c)
    print(iter(c))
    print(list(c))

print()


# 예제 3
# read() : 전체 읽기 / read(10) : 10 byte 읽어오기
# 커서가 있다
with open('./resource/it_news.txt', 'r', encoding='UTF-8') as f:
    c = f.read(20)
    print(c)
    c = f.read(20)
    print(c)
    c = f.read(20)
    print(c)
    f.seek(0,0)
    c = f.read(20)
    print(c)

print()


# 예제 4  -  라인 한줄 한줄 읽기
with open('./resource/it_news.txt', 'r', encoding='UTF-8') as f:
    c = f.readline()
    print(c)
    c = f.readline()
    print(c)


# 예제 5  -  readlines (전체를 읽은 후 라인 단위 리스트로 저장)
with open('./resource/it_news.txt', 'r', encoding='UTF-8') as f:
    cts1 = f.readlines()
    print(cts1, type(cts1))
    print()
    for c in cts1:
        print(c, end='')





# 파일 쓰기 - 우리가 쓰고자 하는 가상의 파일을 연결할 때에도 open 씀
# 예제 1
with open('./resource/contents.txt', 'w') as f:
    f.write('I love you\n')

# 예제 2
with open('./resource/contents.txt', 'a') as f:
    f.write('I love you one more time\n')

# 예제 3  -  writelines : 리스트 -> 파일
with open('./resource/contents2.txt', 'w') as f:
    list = ['Orange\n', 'Kong\n', 'Gyeong-gi\n']
    f.writelines(list)

# 예제 4
with open('./resource/contents3.txt', 'w') as f:
    print('Test Text Write!', file=f)
    print('Test Text Write!', file=f)
    print('Test Text Write!', file=f)