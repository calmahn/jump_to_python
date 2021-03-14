#Formatting 문자열 안의 특정한 값 변경, 문자열 안에 어떤 값을 삽입

a = "I eat %d apples." %3
print(a)

b = "I eat %s apples." %"three"
print(b)

number = 3
c = "I eat %d apples." %number
print(c)