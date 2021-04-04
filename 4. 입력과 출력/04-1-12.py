a = 1
def vartest(a):
    a = a+1
    return a

a = vartest(a)
print(a)


b = 1
def vartest2():
    global b
    b = b+1

vartest2()
print(b)