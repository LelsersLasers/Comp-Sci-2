class Counter(object):
    """An object that keeps track of some value, where the value starts at zero,
    counts up to some maximum value, and then resets back to zero."""

    def __init__(self, maxValue):
        self.maxValue = maxValue
        self.value = 0

    def __str__(self):
        returnVal = "Value:%i   (MaxValue = %i)" % (self.value, self.maxValue)
        return returnVal

    def increment(self):
        self.value = self.value + 1
        if self.value >= self.maxValue:
            self.value = 0
            return True
        return False

    def setValue(self, newValue):
        self.value = newValue

    def getValue(self):
        return self.value


if __name__ == "__main__":  # test code goes here for custom Classes

    c = Counter(60)
    print(c)
    for i in range(10):
        c.increment()
        print(c)

    print("-" * 20)
    print("set counter value to 55")

    c.setValue(55)
    print(c)
    for i in range(10):
        c.increment()
        print(c)
