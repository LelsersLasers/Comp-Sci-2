"""
    Description: Another fractal that exhibits the property of self-similarity is
                 the Sierpinski triangle. The Sierpinski triangle illustrates a
                 three-way recursive algorithm. The first thing sierpinski does is
                 draw the outer triangle. Next, there are three recursive calls, one
                 for each of the new corner triangles we get when we connect the midpoints.

                 Look at the code and think about the order in which the triangles
                 will be drawn. While the exact order of the corners depends upon
                 how the initial set is specified, let’s assume that the corners
                 are ordered lower left, top, lower right.

                 Because of the way the sierpinski function calls itself, sierpinski
                 works its way to the smallest allowed triangle in the lower-left
                 corner, and then begins to fill out the rest of the triangles working
                 back. Then it fills in the triangles in the top corner by working
                 toward the smallest, topmost triangle. Finally, it fills in the lower-right
                 corner, working its way toward the smallest triangle in the lower right.
    Author: Mr. Bloom
    Date: Fall 2021
"""

import turtle

#------------------------------------------------------------------------------#
def drawTriangle(points, color, myTurtle):
    myTurtle.fillcolor(color)
    myTurtle.up()
    myTurtle.goto(points[0][0],points[0][1])
    myTurtle.down()
    myTurtle.begin_fill()
    myTurtle.goto(points[1][0],points[1][1])
    myTurtle.goto(points[2][0],points[2][1])
    myTurtle.goto(points[0][0],points[0][1])
    myTurtle.end_fill()
    return

#------------------------------------------------------------------------------#
def getMid(p1, p2):
    """
    this function takes as arguments two endpoints and returns the point halfway
    between them. In addition, this program has a function that draws a filled
    triangle using the begin_fill and end_fill turtle methods.
    """
    return ( (p1[0]+p2[0]) / 2, (p1[1] + p2[1]) / 2)

#------------------------------------------------------------------------------#
def sierpinski(points, degree, myTurtle):

    colormap = ["blue", "red", "green", "white", "yellow", "violet", "orange"]

    # Draw the outer triangle first
    drawTriangle(points, colormap[degree], myTurtle)

    # Then, there are three recursive calls, one for each of the
    # new corner triangles we get when we connect the midpoints.
    if degree > 0:
        sierpinski([points[0],
                        getMid(points[0], points[1]),
                        getMid(points[0], points[2])],
                   degree-1, myTurtle)
        sierpinski([points[1],
                        getMid(points[0], points[1]),
                        getMid(points[1], points[2])],
                   degree-1, myTurtle)
        sierpinski([points[2],
                        getMid(points[2], points[1]),
                        getMid(points[0], points[2])],
                   degree-1, myTurtle)

#------------------------------------------------------------------------------#
def main():
   myTurtle = turtle.Turtle()
   myWin = turtle.Screen()
   myPoints = [[-100,-50],[0,100],[100,-50]]
   sierpinski(myPoints,3,myTurtle)
   myWin.exitonclick()


main()
