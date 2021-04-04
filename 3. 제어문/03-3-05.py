marks = [90, 25, 67, 45, 80]
for number in range(len(marks)):
    if marks[number] < 60: continue
    print("%d번 학생 축하합니다. 합격입니다." %(number + 1))

#len - 리스트 안의 요소 개수 리턴
#len(marks) ==> 5
#range(len(marks)) ==> range(5)