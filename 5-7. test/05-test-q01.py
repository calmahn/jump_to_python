class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val
        return(val)

class UpgradeCalculator(Calculator):
    def minus(self, val):
        self.value -= val
        return(val)

cal = UpgradeCalculator()
print(cal.add(10))
print(cal.minus(7))