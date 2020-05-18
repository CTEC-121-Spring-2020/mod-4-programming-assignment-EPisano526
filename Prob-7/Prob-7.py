# Module 5
#   Programming Assignment 6
#       Prob-7.py

# Esther Pisano

from graphics import *


def face():
    win = GraphWin("Face", 400, 400)

    # First make hair because it will be behind the head
    top_hair = Circle(Point(175, 80), 65)
    top_hair.setFill("black")
    top_hair.draw(win)

    top_hair2 = top_hair.clone()
    top_hair2.move(50, 0)
    top_hair2.draw(win)

    backhair = Rectangle(Point(290, 280), Point(110, 80))
    backhair.setFill("black")
    backhair.draw(win)

    # Face
    faces = Oval(Point(280, 230), Point(120, 40))
    faces.setFill("navajowhite")
    faces.draw(win)

    # Eyes
    left_eye = Circle(Point(165, 120), 20)
    left_eye.setFill("white")
    left_eye.setOutline("white")
    left_eye.draw(win)

    right_eye = left_eye.clone()
    right_eye.move(70, 0)
    right_eye.draw(win)

    # Pupils
    left_pupil = Circle(Point(172, 127), 7)
    left_pupil.setFill("black")
    left_pupil.draw(win)

    right_pupil = left_pupil.clone()
    right_pupil.move(55, 0)
    right_pupil.draw(win)

    # Nose
    nose = Line(Point(190, 150), Point(200, 140))
    nose.setWidth(5)
    nose.draw(win)

    nose2 = Line(Point(210, 150), Point(200, 140))
    nose2.setWidth(5)
    nose2.draw(win)

    # Mouth
    mouth1 = Line(Point(179, 180), Point(220, 180))
    mouth1.setWidth(7)
    mouth1.setOutline("red")
    mouth1.draw(win)

    mouth2 = Line(Point(180, 181), Point(175, 175))
    mouth2.setWidth(7)
    mouth2.setOutline("red")
    mouth2.draw(win)

    mouth3 = Line(Point(221, 181), Point(216, 175))
    mouth3.setWidth(7)
    mouth3.setOutline("red")
    mouth3.draw(win)

    # Teeth
    teeth = Rectangle(Point(207, 190), Point(191, 180))
    teeth.setFill("white")
    teeth.setOutline("white")
    teeth.draw(win)

    line = Line(Point(199, 190), Point(199, 180))
    line.draw(win)

    # Ears
    ear1 = Oval(Point(290, 170), Point(270, 120))
    ear1.setFill("navajowhite")
    ear1.setOutline("navajowhite")
    ear1.draw(win)

    ear2 = ear1.clone()
    ear2.move(-160, 0)
    ear2.draw(win)

    # Earrings
    earring = Circle(Point(280, 165), 3)
    earring.setOutline("aqua")
    earring.setFill("aqua")
    earring.draw(win)

    earring2 = earring.clone()
    earring2.move(-160, 0)
    earring2.draw(win)

    input()
    win.getmouse()
    win.close()


face()
