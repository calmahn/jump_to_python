a, b = ('python','life')
print(a); print(b)
print(a,b)

(c, d) = 'python','life'
print(c); print(d)
print(c, d)

[e, f] = ['python','life']
print(e); print(f)
print(e, f)

g = 3
h = 5
g,h = h,g
print(g); print(h)

i = [1,2,3]
j = [1,2,3]
print(i is j)
#서로 다른 메모리를 가지기 때문