y = 3.42134234
a = "{0:0.4f}" .format(y)
print(a)

b = "{0:10.4f}" .format(y)
print(b)

# {} 포매팅 문자가 아닌 문자 그대로 사용할 때
c = "{{ and }}" .format()
print(c)