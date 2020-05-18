# Module 5
#   Programming Assignment 6
#       Prob-4.py

# Esther Pisano


from graphics import*


def main():

    # window and loop was made to go through if elif.
    win = GraphWin("House", 200, 200)
    for i in range(6):
        win.getMouse()

        # FIRST CLICK
        # starting from bottom left of win make line straight up and
        # to the side
        if i == 1:
            first_line = Line(Point(25, 175), Point(175, 175))
            first_line.draw(win)
            second_line = Line(Point(25, 175), Point(25, 75))
            second_line.draw(win)

        # SECOND CLICK
        # To create a rectangle with above lines, i calculated
        # the previous verticle line top point and connected it to
        # its other two points
        elif i == 2:
            first_line = Line(Point(175, 75), Point(175, 175))
            first_line.draw(win)
            second_line = Line(Point(175, 75), Point(25, 75))
            second_line.draw(win)

        # DOOR CLICK
        # Calculated the length of the rectangle to find 1/5 of the length
        # Made the top line and used that to draw lines down from the edges
        # of it to the bottom of house
        elif i == 3:
            door_top = Line(Point(50, 125), Point(80, 125))
            door_top.draw(win)
            door_left = Line(Point(50, 125), Point(50, 175))
            door_left.draw(win)
            door_right = Line(Point(80, 125), Point(80, 175))
            door_right.draw(win)

        # WINDOW CLICK
        # used half the widtch of the door to make the window.
        # calculated that length to make a square
        elif i == 4:
            window_top = Line(Point(125, 120), Point(140, 120))
            window_top.draw(win)
            window_left = Line(Point(125, 120), Point(125, 135))
            window_left.draw(win)
            window_right = Line(Point(140, 120), Point(140, 135))
            window_right.draw(win)
            window_bottom = Line(Point(125, 135), Point(140, 135))
            window_bottom.draw(win)

        # ROOF CLICK
        # found the middle of house point by adding the half of the
        # rectangle length by the first click- first point x value.
        elif i == 5:
            roof_right = Line(Point(100, 25), Point(175, 75))
            roof_right.draw(win)
            roof_left = Line(Point(100, 25), Point(25, 75))
            roof_left.draw(win)


main()
