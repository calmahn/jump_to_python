#List comprehension

a = [1,2,3,4]
result = []
for num in a:
    result.append(num*3)

print(result)

b = [1,2,3,4]
result2 = [num*3 for num in a]
print(result2)


c = [1,2,3,4]
result3 = [num*3 for num in a if num%2 == 0]
print(result3)


result4 = [x*y for x in range(2,10) for y in range(1,10)]
print(result4)