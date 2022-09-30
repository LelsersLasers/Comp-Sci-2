from counter import *

class Clock(object):
    """ a 24-hour clock object, made of three counter objects: one for the seconds
        (0->59), one for the minutes (0->59), and one for the hour (0->23).  """

    def __init__(self, hour, min, sec):
        """ construct counter obj, given hours minutes and seconds """
        self.hourCounter = Counter(24)
        self.hourCounter.setValue(hour)
        self.minCounter = Counter(60)
        self.minCounter.setValue(min)
        self.secCounter = Counter(60)
        self.secCounter.setValue(sec)
    def __str__(self):
        returnVal = "Clock: %i:%i:%i" % (self.hourCounter.value, self.minCounter.value, self.secCounter.value)
        return returnVal
    def getTime(self):
        returnVal = "%i:%i:%i" % (self.hourCounter.value, self.minCounter.value, self.secCounter.value)
        return returnVal
    def getHour(self):
        return self.hourCounter.getValue()
    def getMin(self):
        return self.minCounter.getValue()
    def getSec(self):
        return self.secCounter.getValue()
    def setHour(self, newValue):
        self.hourCounter.setValue(newValue)
    def setMin(self, newValue):
        self.minCounter.setValue(newValue)
    def setSec(self, newValue):
        self.secCounter.setValue(newValue)
    def tick(self):
        if self.secCounter.increment():
            if self.minCounter.increment():
                self.hourCounter.increment()



if __name__ == "__main__":
    c1 = Clock(12,55,21)
    print(c1)
    print("Setting time to 23:59:55...")
    c1.setHour(23)
    c1.setMin(59)
    c1.setSec(55)
    print("Hour for c1: %d" % (c1.getHour()))
    print(c1)
    for i in range(15):
        c1.tick()
        print(c1)
