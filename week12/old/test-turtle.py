"""
    Description: This program is just for testing your implementation of the
                 Turtle class (zturtle.py). You'll know if your ZTurtle class is
                  working properly after you run this program.
    Author: Mr. Bloom
    Date: Spring 2020
"""

from zturtle import *
from graphics import *

def drawO(turtle, window):
    currWidth = turtle.x
    currHeight = turtle.y
    turtle.moveTo(currWidth+35,currHeight-40)
    turtle.setHeading(270)
    for i in range(1200):
        if i % 15 == 0:
            turtle.dot()
        turtle.forward(2)
        turtle.turn(2.5)
        if window.checkMouse():
            return


def drawL(turtle):
    currWidth = turtle.x
    currHeight = turtle.y
    turtle.moveTo(currWidth+35,currHeight)
    turtle.setHeading(0)
    turtle.forward(50)
    turtle.dot()
    currWidth = turtle.x
    currHeight = turtle.y
    turtle.moveTo(currWidth-50, currHeight)
    turtle.turn(90)
    turtle.forward(-100)
    turtle.dot()
    turtle.moveTo(currWidth, currHeight)



def drawE(turtle):
    currWidth = turtle.x
    currHeight = turtle.y
    turtle.moveTo(currWidth+35,currHeight)
    turtle.setHeading(90)
    turtle.dot()
    turtle.forward(-100)
    turtle.dot()
    turtle.turn(-90)
    turtle.forward(35)
    turtle.dot()
    currWidth = turtle.x
    currHeight = turtle.y
    turtle.moveTo(currWidth, currHeight+50)
    turtle.dot()
    turtle.setHeading(180)
    turtle.forward(35)
    currWidth = turtle.x
    currHeight = turtle.y
    turtle.moveTo(currWidth, currHeight+50)
    turtle.turn(180)
    turtle.forward(35)
    turtle.dot()

def drawH(turtle):
    turtle.setHeading(90)
    turtle.dot()
    turtle.down()
    turtle.forward(100)
    turtle.dot()
    currWidth = turtle.x
    currHeight = turtle.y
    turtle.moveTo(currWidth,currHeight-50)
    turtle.setHeading(0)
    turtle.down()
    turtle.forward(50)
    turtle.turn(-90)
    turtle.forward(50)
    turtle.dot()
    turtle.turn(180)
    turtle.forward(100)
    turtle.dot()


def main():

    gw = GraphWin("zturtle test", 800, 600)
    gw.setBackground("black")

    turtle = ZTurtle(100, 100, gw)
    print(turtle)

    drawH(turtle)
    drawE(turtle)
    drawL(turtle)
    drawL(turtle)
    drawO(turtle, gw)

    gw.close()


main()
