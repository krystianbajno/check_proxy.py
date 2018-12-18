class Counter(object):
    def __init__(self):
        self.count = 0
        self.found = 0

    def addCount(self):
        self.count = self.count+1
        
    def addFound(self):
        self.found = self.found+1

    def getFound(self):
        return self.found
    
    def getCount(self):
        return self.count
    
   