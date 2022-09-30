class Pizza(object):
    """ class for a single pizza object """
    def __init__(self, type):
        self.type = type
        self.slices = 8
    def __str__(self):
        returnVal = "%s pizza :: slices left = %i" % (self.type, self.slices)
        return returnVal
    def getSlices(self):
        return self.slices
    def getTopping(self):
        return self.type
    def eatSlice(self):
        if self.slices == 0:
            print("No slices left... :(")
        else:
            self.slices = self.slices - 1



if __name__ == "__main__":
    p1 = Pizza("cheese")
    p2 = Pizza("mushroom and onion")
    print(p1)
    print(p2)

    print("-" * 20)
    print("Num slices left in p2: %s" % p2.getSlices())
    print("Eating a slice of %s!" % p2.getTopping())
    p2.eatSlice()
    print(p2)

    print("-" * 20)
    for i in range(10):
        print("Eating a slice of %s!" % p1.getTopping())
        p1.eatSlice()
        print(p1)
