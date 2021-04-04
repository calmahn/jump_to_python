a = [1,2,3]
b = a[:]
a[1] = 4

print(a); print(b)

from copy import copy
c = [1,2,3]
d = copy(c)
print(d)

print(c is d)