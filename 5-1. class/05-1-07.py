#클래스 변수

class Family:
    lastname = "김"

print(Family.lastname)

a = Family()
b = Family()
Family.lastname = "박"
print(a.lastname); print(b.lastname)