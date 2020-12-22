from figures import Rectangle, Square, Circle

rect_1 = Rectangle(3, 4)
rect_2 = Rectangle(12, 5)
print(rect_1.get_area(), rect_2.get_area())

square_1 = Square(5)
square_2 = Square(10)
print(square_1.get_area(), square_2.get_area())

circle_1 = Circle(12)
circle_2 = Circle(7)
print(circle_1.get_area(), circle_2.get_area())

figures = [rect_1, rect_2, square_1, square_2, circle_1, circle_2]
for figure in figures:
    print(figure.get_area())
