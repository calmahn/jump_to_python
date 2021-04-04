a = "hobby"
b = a.count('b')
print(b)

c = "Python is the best choice"
d = c.find('b')
e = c.find('k') #존재하지 않는다면 -1 반환
print(d); print(e)

f = "Life is too short"
g = f.index('t')
h = f.index('k')
print(g); print(h)