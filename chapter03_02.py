# 파이썬 문자형
# 중요

# 문자열 생성
str1 = "I am Python"
str2 = 'Python'
str3 = """How are you?"""
str4 = '''Thank you!'''

print(len(str1))
print(len(str2))

# 빈 문자열 생성
str1_t1 = ''
str2_t2 = str()

print(type(str1_t1), len(str2_t2))

# 이스케이프 문자 사용
# print('I'm boy')  -> error!
print('I\'m Boy') # \를 특수문자 앞에 둠으로서 해당 특수문자를 출력하게끔
print('a \t b')   # tab 키만큼 띄우기
print('a\nb') # 행 바꾸기

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

escape_str1 = "Do you have a \"retro games?\"?"
escape_str2 = "What do you like? \nI like boobs"
print(escape_str1)
print(escape_str2)

# Raw String 출력 -> \ 를 피하기 위해(파일저장위치)
raw_s1 = r'D:\python\test'
print(raw_s1)

# 멀티라인 입력 - 줄바꿔서 입력하고싶을때 \를 추가함으로서 print문이 바로 바인딩된다는 것을 알려줌
multi_str = "aivfvkafbvurvalkfjvbaivkjafbfiluvbajkvlbfjvbawoivjavfnviae;bvejfkavlfvbaeifvlakefjbvaefivlbefivb"
multi_str_1 = \
"""
안녕하십니까, 오늘의 날씨입니다.
오늘은 비교적 추운 날들이 이어지겠습니다.
빙판길 조심하시길 바랍니다.
"""
print(multi_str)
print(multi_str_1)

# 문자열 연산
str_o1 = "python"
str_o2 = "Apple"
str_o3 = "I would like to have a new iPad"
str_o4 = "Sinsa Nonhyeon Gangnam"

print(str_o1 * 3)
print(str_o1 + str_o2)
print('i' in str_o3)
print('W' in str_o3) #대,소문자 구분함
print('Z' not in str_o3)

#문자열 형 변환
print(str(66), type(str(66)))
print(str(10.1))
print(type(True))
print(type(str(True)))

# 문자열 함수(upper, isalnum, startswith, count, endswith, isalpha...)
print("Capitalize: ", str_o1.capitalize())
print("endswith: ", str_o2.endswith("e")) # 마지막 문자가 무엇인지
print("replace: ", str_o2.replace("pp", "ooo"))
print("sorted: ", sorted(str_o2))
print("class sorted: ", type(sorted(str_o2)))
print("split: ", str_o4.split(" "))
print("class split: ", type(str_o4.split(" ")))


# 반복(시퀀스)
im_str = "Good boy"
print(dir(im_str))

for i in im_str:
    print(i)

# 슬라이싱
str_s1 = "Nice Scotty"

# 슬라이싱 연습 - 왼쪽부터 (오른쪽-1)까지 나와라
# 문장에서 원하는 단어만 뽑아내기
print(len(str_s1))
print(str_s1[0:3]) # 0 1 2
print(str_s1[5:11])
print(str_s1[5:])
print(str_s1[:len(str_s1)])
print(str_s1[1:11:2]) # 2칸씩 가져와라
print(str_s1[0:11:3])
print(str_s1[-2:])
print(str_s1[::2])
print(str_s1[::-1])

