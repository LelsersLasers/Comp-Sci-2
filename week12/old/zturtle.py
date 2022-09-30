"""
    Description: turtle class using Zelle graphics (only partially complete).
    Author: Mr. Bloom
    Date: Spring 2020
"""

from graphics import *
from math import *
from time import sleep

###############################################################

class ZTurtle(object):
    """ Zelle Graphics Turtle """
    # dot         drop a visible marker at current location
    def __init__(self, x, y, gw):
        self.x = x
        self.y = y
        self.heading = 0
        self.tailup = False
        self.window = gw
        self.color = "green"
    def __str__(self):
        returnVal = "(X: %i, Y: %i)  Heading: %i\nTailup: %s  Color %s" % (self.x, self.y, self.heading, self.tailStatus(), self.color)
        return returnVal
    def down(self):
        self.tailup = False
    def up(self):
        self.tailup = True
    def setHeading(self, heading):
        self.heading = heading
    def setColor(self, color):
        self.color = color
    def moveTo(self, x, y):
        self.x = x
        self.y = y
    def turn(self, angle):
        self.heading = self.heading + angle
    def left(self, angle):
        self.heading = self.heading - angle
    def tailStatus(self):
        if self.tailup:
            return "up"
        return "down"
    def dot(self):
        print("??")

    def forward(self, ds):
        """ move forward a distance ds, draw if tail is down """
        curr_pt = Point(self.x, self.y)
        theta = radians(self.heading)
        dx = ds * cos(theta)
        dy = ds * sin(theta)
        nx = self.x + dx
        ny = self.y + dy
        new_pt = Point(nx, ny)
        if not self.tailup:
            L = Line(curr_pt, new_pt)
            L.draw(self.window)
            L.setFill(self.color)
            sleep(0.1)
        self.x = nx
        self.y = ny


#------------------------------------------------------------------------------#

if __name__ == "__main__":
    gw = GraphWin("zturtle test", 500, 500)
    gw.setBackground("gray")
    t = ZTurtle(100,100,gw)
    print(t)
    t.down()
    t.forward(100)
    gw.getMouse()
