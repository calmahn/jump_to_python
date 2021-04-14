#abs 절댓값
print(abs(3)); print(abs(-3.5))

#all 모두 참이면 Treu / 하나라도 거짓이 있으면 False
print(all([0,3,4,5]))

#any 하나라도 참이면 True / 모두 거짓일 때 False
print(any([1,2,3,0]))

#dir
print(dir([1,2,3]))

#divmod a를 b로 나는 몫과 나머지를 튜플 형태로 돌려줌
print(divmod(7,3))

#enumerate 순서가 있는 자료형을 입력으로 받아 인덱스 값을 포함하는 enumerate 객체를 돌려줌
for i, name in enumerate(['body','foo','bar']):
    print(i, name)

#eval(expression) 실행 가능한 문자열을 입력으로 받아 문자열 실행한 결괏값 돌려줌
print(eval('1+2')); print(eval("'hi'+'a'")); print(eval('divmod(4,3)'))

#filter
def positive(l):
    result = []
    for i in l:
        if i>0:
            result.append(i)
    return result

print(positive([1,-3,2,0,-5,6]))

def positive2(x):
    return x>0

print(list(filter(positive2, [1,-3,2,0,-5,6])))
print(list(filter(lambda x: x>0,[1,-3,2,0,-5,6])))

#int
print(int('11',2)); print(int('1A',16))

#list
print(list("python"))

#pow 제곱
print(pow(2,4))

#range
print(list(range(5)))
print(list(range(5,10)))
print(list(range(1,10,2))) #숫자 사이의 거리

#round
print(round(5.678,2))

#sorted
print(sorted("zero"))

#type
print(type("abd"))
print(type([]))