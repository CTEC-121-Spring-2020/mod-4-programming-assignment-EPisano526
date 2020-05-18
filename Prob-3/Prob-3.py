# Module 5
#   Programming Assignment 6
#       Prob-3.py

# Esther Pisano

from graphics import *


def main():
    # create winGraph
    # made a radius number
    win = GraphWin("Archery Target", 200, 200)
    center = Point(100, 100)
    radius = 10

    # white circle. Largest and furthest back
    white = Circle(center, radius * 5)
    white.draw(win)

    # Black circle
    black = Circle(center, radius * 4)
    black.setFill("black")
    black.draw(win)

    # Blue Circle
    blue = Circle(center, radius * 3)
    blue.setFill("blue")
    blue.setOutline("blue")
    blue.draw(win)

    # Red circle
    red = Circle(center, radius * 2)
    red.setFill("red")
    red.setOutline("red")
    red.draw(win)

    # Yellow target
    yellow = Circle(center, radius * 1)
    yellow.setFill("yellow")
    yellow.setOutline("yellow")
    yellow.draw(win)


main()
