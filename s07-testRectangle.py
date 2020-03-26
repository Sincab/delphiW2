from Rectangle import Rectangle

def main():
    # Create a circle with radius 1
    rect1 = Rectangle(2,9)
    print("The area of the rectangle of width:",
        rect1.width, "is", rect1.getArea())

    rect2 = Rectangle(5, 9)
    print("The area of the rectangle of width:",
          rect2.width, "is", rect2.getArea())


main() # Call the main function
