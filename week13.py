from random import randint

class RandMemory(object):

    
    def __init__(self,minimum,maximum):
        self.listri = []
        self.minimum = minimum
        self.maximum = maximum

    @property
    def get(self):
        self.ri = randint(self.minimum, self.maximum)        
        self.listri.append(self.ri) 
        return self.ri

    def history(self):
        print(self.listri)

r = RandMemory(1, 100)
print(r.get)
print(r.get)
print(r.get)
r.history()

