a = "I eat {0} apples" .format("3")
print(a)

b = "I eat {0} apples" .format("five")
print(b)

number = 3
c = "I eat {0} apples" .format(number)
print(c)

day = "three"
d = "I ate {0} apples. so I was sick for {1} days." .format(number, day)
print(d)

e = "I ate {number} apples. so I was sick for {day} days." .format(number=10, day=3)
print(e)

f = "I ate {0} apples. so I was sick for {day} days." .format(10, day = 3)
print(f)

g = "{0:<10}" .format("hi")
print(g)

h = "{0:>10}" .format("hi")
print(h)

i = "{0:^10}" .format("hi")
print(i)

j = "{0:=^10}" .format("hi")
print(j)

k = "{0:!<10}" .format("hi")
print(k)