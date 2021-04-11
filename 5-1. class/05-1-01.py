class FourCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second  #Method 클래스 안에 구현된 함수

a = FourCal()
a.setdata(4,2)
print(a.first); print(a.second)

c = FourCal()
d = FourCal()
c.setdata(4,2); print(c.first)
d.setdata(3,7); print(d.first)
print(id(c.first)); print(id(d.first))