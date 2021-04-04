#My answer
a = {'A':90, 'B':80, 'C':70}
result = a['B']
del a['B']
print(a)
print(result)

#ex
c = {'A':90, 'B':80, 'C':70}
result2 = c.pop('B')
print(c)
print(result2)