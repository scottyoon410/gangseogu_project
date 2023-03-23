# CSV 파일 읽기 및 쓰기
# CSV : MEME - text/csv

import csv

# 예제 1
with open('./resource/test1.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)                    # 헤더 스킵(목록명 스킵)

    # 객체 확인
    print(reader)
    print(type(reader))

    # 속성값 확인
    print(dir(reader))              # __iter__ 가 있으니까 for 문에서 사용할 수 있구나
    print()

    for c in reader:
        # print(c)
        # print(type(c))
        print(':'.join(c))


# 예제 2
with open('./resource/test2.csv', 'r') as f:
    reader = csv.reader(f, delimiter='|')

    for c in reader:
        print(c)


# 예제 3
with open('./resource/test1.csv', 'r') as f:
    reader = csv.DictReader(f)
    print(reader)
    print(type(reader))
    print(dir(reader))
    print()

    for c in reader:
        for k, v in c.items():
            print(k, ":", v)
        print('---------------')



# 예제 4
w = [[1,2,3], [4,5,6], [7,8,9], [10,11,12], [13,14,15], [16,17,18], [19,20,21]]

with open('./resource/write1.csv', 'w', encoding='UTF-8') as f:
    print(dir(csv))
    wt = csv.writer(f)

    # dir 확인
    print(dir(wt))

    for v in w:
        wt.writerow(v)


# 예제 5
with open('./resource/write2.csv', 'w', encoding='UTF-8') as f:
    fields = ["One", "Two", "Three"]

    wt = csv.DictWriter(f, fieldnames=fields)
    wt.writeheader()

    for v in w:
        wt.writerow({'One':v[0], 'Two':v[1], 'Three':v[2]})