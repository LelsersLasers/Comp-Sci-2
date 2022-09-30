from graphics import *
from alarmclock import *
from time import sleep


def main():

    width = 300
    height = 100
    gw = GraphWin("alarm clock", width, height)
    gw.setBackground("black")

    hours = 23
    minutes = 59
    seconds = 58
    digClock = AlarmClock(hours, minutes, seconds)

    # SET ALARM TIME
    digClock.findAlarmTime("alarm-data.txt")
    
    while True:
        # get current time and display clock
        time = digClock.getTime()
        clockText = Text(Point(width/2, height/2), time)
        clockText.setSize(36)
        clockText.setOutline("green")
        clockText.draw(gw)

        sleep(0.9)        # sleep for 1 second and tick the clock forward one sec
        if digClock.tick() and digClock.getSec() % 2 == 0: # flash for just 10 seconds 
            gw.setBackground("red")
        else:
            gw.setBackground("black")

        clockText.undraw()  # undraw old time, so can display the new time

        if gw.checkMouse():
            break

    gw.close()

if __name__ == "__main__":
    main()
