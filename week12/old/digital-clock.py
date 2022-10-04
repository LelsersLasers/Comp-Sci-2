from graphics import *
from clock import *
from time import sleep


def main():
    width = 300
    height = 100
    gw = GraphWin("digital clock", width, height)
    gw.setBackground("black")

    hours = 23
    minutes = 59
    seconds = 55
    digClock = Clock(hours, minutes, seconds)
    while True:
        # get current time and display clock
        time = digClock.getTime()
        clockText = Text(Point(width/2, height/2), time)
        clockText.setSize(36)
        clockText.setOutline("green")
        clockText.draw(gw)

        sleep(1)        # sleep for 1 second and tick the clock forward one sec
        digClock.tick()

        clockText.undraw()  # undraw old time, so can display the new time

        if gw.checkMouse():
            break

    gw.close()

if __name__ == "__main__":
    main()
