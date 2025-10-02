class strClass:
    def __init__(self, getSting):
        self.getString = getSting

    def printString(self):
        print(self.getString)

x = strClass(input())
x.printString()