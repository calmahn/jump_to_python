#continue: while문을 빠져나가지 않고 맨 처음(조건문)으로 다시 돌아가는 방법

a = 0
while a < 10:
    a = a + 1
    if a%2 == 0: continue
    print(a)


b = 0
while b < 10:
    b = b + 1
    if b%3 == 0: continue
    print(b)