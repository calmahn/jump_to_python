def getTotalPage(m,n):
    if m%n == 0:
        return m // n
    else:
        return m // n + 1

print(getTotalPage(5,20))