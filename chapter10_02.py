# 행맨 만들기

import time
import csv
import random

# 처음 인사
name = input("What is your name? ")

print("Hi,", name, "It's time to play game")

print()

time.sleep(1)

print("Start Loading...")
print()
time.sleep(0.5)

# csv 단어 리스트
words = []

# 문제 csv 파일 로드
with open('./resource/word_list.csv', 'r') as f:
    reader = csv.reader(f)
    # 헤더 스킵
    next(reader)
    for c in reader:
        words.append(c)

# 리스트 섞기
random.shuffle(words)

q = random.choice(words)

print(f'Hint : {q[1]}')


# 정답 단어
word = q[0].strip()

# 추측 단어
guesses = ''

# 기회
turns = 10

# 핵심
# 찬스 카운트가 남아 있을 경우
while turns > 0:
    # 실패 횟수(단어의 매치 수)
    failed = 0

    # 정답 단어 반복
    for char in word:
        # 정답 단어 내에 추측 문자가 포함되어 있는 경우
        if char in guesses:
            # 추측 단어 출력
            print(char, end ="")
        else:
            # 틀린 경우 대시로 처리
            print("_", end=" ")
            failed += 1
    # 단어 추측이 성공한 경우
    if failed == 0:
        print()
        print()
        print('Congratulation! You are the winner!')
        break
    print()

    # 추측 단어 문자 단위 입력
    print()
    guess = input("Guess a character : ")

    # 단어 더하기
    guesses += guess

    # 정답 단어에 추측한 문자가 포함되어 있지 않으면
    if guess not in word:
        turns -= 1
        # 오류 메세지
        print("Ooops! Wrong!")
        # 남은 기회 출력
        print(f'You have {turns} more guesses')

        if turns == 0:
            print(f'{name}! You\'ve failed!!')