from random import randint

class RandMemory(object):

    def __init__(self,minimum,maximum):

        self.minimum = minimum
        self.maximum = maximum

    @property
    def get(self):
        return randint(self.minimum, self.maximum)        

r = RandMemory(1, 100)
print(r.get)
print(r.get)
print(r.get)
