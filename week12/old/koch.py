from zturtle import *
from graphics import *


def koch(t, gw, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch(t, gw, order - 1, size / 3)
            t.left(angle)


def main():

    gw = GraphWin("koch", 800, 600)
    gw.setBackground("black")

    turtle = ZTurtle(0, 550, gw)

    koch(turtle, gw, 5, 800)

    gw.getMouse()


main()
