# Module 5
#   Programming Assignment 6
#       Prob-6.py

# Esther Pisano

from graphics import *


def main():
    win = GraphWin("Legos", 600, 600)

    # Navy blue lego.
    first_sq = Rectangle(Point(62, 62), Point(37, 50))
    first_sq.setWidth(3)
    first_sq.setFill("royalblue")
    first_sq.draw(win)

    for i in range(1, 5):
        next_sq = first_sq.clone()
        next_sq.move(50 * i, 0)
        next_sq.draw(win)

    base_lego = Rectangle(Point(275, 150), Point(25, 60))
    base_lego.setWidth(3)
    base_lego.setFill("royalblue")
    base_lego.draw(win)

    # Green Lego
    tops_green = first_sq.clone()
    tops_green.move(300, 0)
    tops_green.setWidth(3)
    tops_green.setFill("forestgreen")
    tops_green.draw(win)

    for g in range(1, 5):
        restofgreens = tops_green.clone()
        restofgreens.move(50 * g, 0)
        restofgreens.draw(win)

    green_lego = base_lego.clone()
    green_lego.move(300, 0)
    green_lego.setWidth(3)
    green_lego.setFill("forestgreen")
    green_lego.draw(win)

    # Yellow Lego
    tops_yellow = first_sq.clone()
    tops_yellow.move(0, 150)
    tops_yellow.setWidth(3)
    tops_yellow.setFill("yellow")
    tops_yellow.draw(win)

    for g in range(1, 5):
        restofyellows = tops_yellow.clone()
        restofyellows.move(50 * g, 0)
        restofyellows.draw(win)

    yellow_lego = base_lego.clone()
    yellow_lego.move(0, 150)
    yellow_lego.setWidth(3)
    yellow_lego.setFill("yellow")
    yellow_lego.draw(win)

    # Red Lego
    tops_red = tops_yellow.clone()
    tops_red.move(300, 0)
    tops_red.setWidth(3)
    tops_red.setFill("red")
    tops_red.draw(win)

    for g in range(1, 5):
        restofreds = tops_red.clone()
        restofreds.move(50 * g, 0)
        restofreds.draw(win)

    red_lego = yellow_lego.clone()
    red_lego.move(300, 0)
    red_lego.setWidth(3)
    red_lego.setFill("red")
    red_lego.draw(win)

    # Sky Blue lego
    tops_sky = tops_yellow.clone()
    tops_sky.move(0, 150)
    tops_sky.setWidth(3)
    tops_sky.setFill("skyblue")
    tops_sky.draw(win)

    for g in range(1, 5):
        restofsky = tops_sky.clone()
        restofsky.move(50 * g, 0)
        restofsky.draw(win)

    sky_lego = yellow_lego.clone()
    sky_lego.move(0, 150)
    sky_lego.setWidth(3)
    sky_lego.setFill("skyblue")
    sky_lego.draw(win)

    # Black Lego
    tops_black = tops_sky.clone()
    tops_black.move(300, 0)
    tops_black.setWidth(3)
    tops_black.setFill("black")
    tops_black.draw(win)

    for g in range(1, 5):
        restofblacks = tops_black.clone()
        restofblacks.move(50 * g, 0)
        restofblacks.draw(win)

    black_lego = sky_lego.clone()
    black_lego.move(300, 0)
    black_lego.setWidth(3)
    black_lego.setFill("black")
    black_lego.draw(win)

    input()
    win.getmouse()
    win.close()


main()
