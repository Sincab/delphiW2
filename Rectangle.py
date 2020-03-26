
#class for rectangle

class Rectangle:
    # Construct a rectangle object
    def __init__(self, w=1, h=2):
        self.width = w
        self.height = h

    def getPerimeter(self):
        return 2 * (self.width + self.height)

    def getArea(self):
        return self.width * self.height

    def setParameters(self, width, height):
        self.width = width
        self.height = height
