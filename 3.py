class Shape:
    def __init__(self, length = 0, width = 0):
        self.length = length
        self.width = width

    def area(self):
        print(self.length * self.width)

class Recrangle(Shape):
    def __init__(self, length = 0, width = 0):
        super().__init__(length, width)
    def area(self):
        print(self.width * self.length)

length, width = input("Print your lenght and width ").split()
length  = int(length)
width   = int(width)

myRectangle = Recrangle(length = length, width = width)
myRectangle.area()

myRectangleDefault = Recrangle()
myRectangleDefault.area()