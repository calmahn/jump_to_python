import time
print(time.time())

a = time.localtime(time.time()); print(a)

b = time.asctime(time.localtime(time.time())); print(b)

c = time.ctime(); print(c)

d = time.strftime('%x',time.localtime(time.time())); print(d)

e = time.strftime('%c',time.localtime(time.time())); print(e)