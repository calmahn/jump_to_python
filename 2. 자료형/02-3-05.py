a = [1,2,3]
a.append(4)
print(a)

b = [1,2,3]
b.append([5,6])
print(b)

c = [1,4,3,2]
c.sort()
print(c)

d = ['a','c','b']
d.sort()
print(d)

e = ['a','b','c']
e.reverse()
print(e)

f = [1,2,3]
g = f.index(3); print(g)
h = f.index(1); print(h)

i = [1,2,3]
i.insert(0,4)
print(i)
i.insert(3,5)
print(i)

j = [1,2,3,1,2,3]
j.remove(3) #리스트에서 첫 번째로 나오는 x를 삭제
print(j)

k = [1,2,3]
k.pop() #맨 마지막 요소를 돌려주고 그 요소 삭제
print(k)

m = [1,2,3]
m.pop(1) #리스트의 x번째 요소를 돌려주고 그 요소 삭제
print(m)

n = [1,2,3,1]
o = n.count(1); print(o) #x의 개수

p = [1,2,3]
p.extend([4,5])
print(p)
q = [6,7]
p.extend(q)
print(p)