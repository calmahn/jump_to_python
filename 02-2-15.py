# f 문자열 포매팅

name = '홍길동'
age = 30
a = f'나의 이름은 {name}입니다. 나이는 {age}입니다.'
print(a)

# f 문자열 포매팅은 표현식을 지원
# 표현식: 변수와 수식을 함께 사용하는 것
b = f'나는 내년이면 {age+1}살이 된다.'
print(b)

d = {'name':'홍길동', 'age':30}
e = f'나의 이름은 {d["name"]}입니다. 나이는 {d["age"]}입니다.'
print(e)

f = f'{"hi":<10}'
g = f'{"hi":>10}'
h = f'{"hi":^10}'
print(f); print(g); print(h)