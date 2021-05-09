class Circle():
    def __init__(self,radius):
        self.radius = radius
    @property
    def diameter(self):
        return 2*self.radius
    

c = Circle(5)
print(c.radius)
print(c.diameter)

c.radius =10
print(c.radius)
print(c.diameter)

c.diametr = 34

print(c.radius)
print(c.diameter)
