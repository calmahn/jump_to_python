a = [1,2,3,['a','b','c']]

b = a[0]; print(b)
c = a[-1]; print(c)
d = a[3]; print(d)

e = a[-1][0]; print(e)
f = a[-1][1]; print(f)
g = a[-1][2]; print(g)

h = [1,2,['a','b',['Life','is']]]
i = h[2][2][0]; print(i)

j = [1,2,3,4,5]
k = j[0:2]; print(k)

l = "12345"
m = l[0:2]; print(m)

n = [1,2,3,4,5]
o = n[:2]; print(o)
p = n[2:]; print(p)

q = n[1:3]; print(q)

r = [1,2,3,['a','b','c'],4,5]
s = r[2:5]; print(s)
t = r[3][:2]; print(t)