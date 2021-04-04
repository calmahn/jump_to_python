#continue: for문 안의 문장을 수행하는 도중 continue -> for문의 처음으로 돌아감

marks = [90, 25, 67, 45, 80]
number = 0
for mark in marks:
    number = number + 1
    if mark < 60: continue
    print("%d번 학생 축하합니다." %number)