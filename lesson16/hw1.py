#1) создать класс треугольник(поля - это стороны, методы - периметр и площадь)(3б)
class triangle:
    def __init__(self, x , y , z):
        self.v = x
        self.w = y
        self.b = z

    def p(self):
        return self.v + self.w + self.b

    def s(self):
        return (self.v + self.w + self.b) / 2

x = int(input(':'))
y = int(input(':'))        
z = int(input(':'))
c1 = triangle(x,y,z)        
print(c1.p())
print(c1.s())