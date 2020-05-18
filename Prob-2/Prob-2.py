# Module 5
#   Programming Assignment 6
#       Prob-2.py

# Esther Pisano

from graphics import *


def main():
    # creating a label "win" for the graph that we wish to draw in.
    # titled it "Squares"
    win = GraphWin("Squares", 200, 200)

    # created first rectangle
    shape = Rectangle(Point(50, 50), Point(20, 20))

    # colored the shape
    shape.setOutline("red")
    shape.setFill("red")

    # executed the drawing function
    shape.draw(win)

    # made a loop to make more rectangles.
    # This will loop 5 times
    for i in range(5):
        p = win.getMouse()
        c = shape.getCenter()
        dx = p.getX() - c.getX()
        dy = p.getY() - c.getY()

    # code below will add the new coordinate to the first coordinate (50,50)
    # it will then create a new rectangle where the new float number is (which is where the mouse was clicked)

        new_shape = Rectangle(Point(50+dx, 50+dy), Point(20+dx, 20+dy))
        new_shape.setOutline("red")
        new_shape.setFill("red")
        new_shape.draw(win)

    # create a label to show window is ending
    label = Text(Point(100, 120), "Click once more to quit")
    label.draw(win)
    win.getMouse()
    win.close()


main()
