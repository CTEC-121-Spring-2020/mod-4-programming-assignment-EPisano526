# Module 5
#   Programming Assignment 6
#       Prob-5.py

# Esther Pisano


from graphics import *


def main():
    win = GraphWin("Car", 500, 200)

    # Rectangle base for car
    car_base = Rectangle(Point(450, 150), Point(75, 100))
    car_base.setFill("red")
    car_base.draw(win)

    # Car top made with lines and thicker width
    car_top = Line(Point(175, 65), Point(325, 65))
    car_top.setOutline("red")
    car_top.setWidth(5)
    car_top.draw(win)

    car_left = Line(Point(125, 100), Point(175, 65))
    car_left.setOutline("red")
    car_left.setWidth(5)
    car_left.draw(win)

    car_right = Line(Point(375, 100), Point(325, 65))
    car_right.setOutline("red")
    car_right.setWidth(5)
    car_right.draw(win)

    # Tires
    radius = 30
    tire_back = Circle(Point(125, 150), radius)
    tire_back.setFill("black")
    tire_back.draw(win)

    tire_front = Circle(Point(375, 150), radius)
    tire_front.setFill("black")
    tire_front.draw(win)

    # Windows
    window_back = Polygon(Point(135, 97), Point(175, 70), Point(
        245, 70), Point(245, 97), Point(135, 97))
    window_back.setFill("black")
    window_back.draw(win)

    window_front = Polygon(Point(365, 97), Point(325, 70), Point(
        255, 70), Point(255, 97), Point(365, 97))
    window_front.setFill("black")
    window_front.draw(win)

    # Bumpers
    bumper_front = Rectangle(Point(455, 148), Point(410, 128))
    bumper_front.setFill("grey")
    bumper_front.draw(win)

    bumper_back = Rectangle(Point(85, 148), Point(70, 128))
    bumper_back.setFill("grey")
    bumper_back.draw(win)

    win.getMouse()
    win.close()


main()
