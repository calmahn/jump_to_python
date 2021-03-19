grade = {'pey':10, 'juliet':99}
print(grade['pey'])
print(grade['juliet'])

a = {1:'a', 2:'b'}
print(a[1]); print(a[2])

b = {'name':'pey','phone':'012345','birth':'1118'}
print(b.keys())

for k in b.keys():
    print(k)

print(list(b.keys()))
print(b.values())
print(b.items())
print(b.get('name'))
print(b.get('nokey'))
print(b.get('foo','bar'))