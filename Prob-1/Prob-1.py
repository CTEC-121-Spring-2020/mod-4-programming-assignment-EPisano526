# Module 5
#   Programming Assignment 6
#       Prob-1.py

# Esther Pisano

# INSTRUCTIONS:
#   Insert a comment above each line of code in the program below to describe
#   what the code does

# library of graphics to import into this sheet
from graphics import *

# opens the main section


def main():

    # creating a label for the graph that we wish to draw in
    win = GraphWin()

   # here we are drawing a circle in the GraphWin where the centerpoint is (50,50)
    # and the radius is 20. We have also labeled this circle "shape"
    shape = Circle(Point(50, 50), 20)

    # We call up the circle "shape" and outline it a red color.
    shape.setOutline("red")

    # We call up the circle "shape" and fill it with color red.
    shape.setFill("red")

    # We command the computer to draw the "shape" in our GraphWin
    shape.draw(win)

    # We create a random i label so the computer and run through this loop 5 times.
    for i in range(5):

        # Here the "p" variable stands for waiting for the user to
        # click the mouse in the window
        p = win.getMouse()

        # returns the clone of the centerpoint of the circle
        c = shape.getCenter()

        # dx is the new variable for the difference between the two X variables in the
        # circles that were made by clicking
        dx = p.getX() - c.getX()

        # dy is the new variable for the difference between the two Y variables in the
        # circles that were made by clicking
        dy = p.getY() - c.getY()

        # directing computer to move circle to the difference of points made by mouse.
        shape.move(dx, dy)

     # Command to close the window
    win.close()


# end of main element.
main()
