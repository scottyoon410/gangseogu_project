# 외장함수(External function)
# 종류 : sys, pickle, shutil, temfile, time, random

# 예제 1
import sys
print(sys.argv)


# 예제 2 (강제 종료)
# sys.exit()


# 예제 3 (파이썬 패키지 위치)
print(sys.path)


# 예제 4 Pickle (객체 파일 쓰기) - 중요!!
import pickle

f = open("test.obj", 'wb')
obj = {1: 'Python', 2:'Study', 3:'Basic'}
pickle.dump(obj, f)
f.close()


# 예제 5 (객체 파일 읽기)
f = open('test.obj', 'rb')
data = pickle.load(f)
print(data, type(data))
f.close()


# os : 환경 변수, 윈도우나 맥에서 할 수 있는 것을 파이썬 코드로 진행할 수 있게 하는 것
# mkdir, rmdir(비어 있으면 삭제), rename

# 예제 6
import os
print(os.environ)
print(os.environ["LOGNAME"])


# 예제 7 (현재 경로)
print(os.getcwd())


# 예제 8 - time : 시간 관련 처리 / 언제 예외가 났는지, 언제 데이터가 삽입이 되었는지
import time

print(time.time())

# 예제 9
print(time.localtime(time.time()))

# 예제 10
print(time.ctime())

# 예제 11 (형식으로 표현)
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))

# 예제 12 (시간 간격 발생)
# for i in range(5):
#     print(i)
#     time.sleep(1)

# 예제 13 - random (난수 관련)
import random
print(random.random())

# 예제 14
print(random.randint(1, 45))        # 1 ~ 45
print(random.randrange(1, 45))      # 1 ~ 44

# 예제 15 - shuffle (섞기)
d = [1, 2, 3, 4, 5]
random.shuffle(d)
print(d)

# 예제 16 (무작위 선택)
c = random.choice(d)
print(c)

# 예제 17 - webbrowser : 본인 os의 웹 브라우저 실행
import webbrowser

webbrowser.open("http://google.com")
webbrowser.open_new_tab("http://google.com")