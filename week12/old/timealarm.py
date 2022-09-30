from clock import *

class Timealarm(object):

    def __init__(self, hour, min, sec):
        self.hour = hour
        self.min = min
        self.sec = sec

    def inAlarm(self, clock):
        startClock = Clock(self.hour, self.min, self.sec)
        for i in range(10):
            if startClock.getTime() == clock.getTime():
                return True
            else:
                startClock.tick()
        return False
    def load(self, nonFormattedString):
        if len(nonFormattedString) >= 5:
            items = nonFormattedString.split(":")
            self.hour = int(items[0])
            self.min = int(items[1])
            self.sec = int(items[2])
    def formatSave(self):
        returnVal = "%i:%i:%i" % (self.hour, self.min, self.sec)
        return returnVal
