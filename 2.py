class Shape:
    def __init__(self, length = 0, width = 0):
        self.length = length
        self.width  = width

    def area(self):
        print(self.length * self.width)


class Square(Shape):
    def __init__(self, length = 0):
        super().__init__(length, length)
    
    def area(self):
        print(self.length ** 2)

length, width = input("Print your lenght and width ").split()
length  = int(length)
width   = int(width)

myShape = Shape(length = length, width = width)
myShape.area()

mySquare = Square(length = length)
mySquare.area()

mySquareDefaultArea = Square()
mySquareDefaultArea.area()