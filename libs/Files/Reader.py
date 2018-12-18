class Reader(object):
    def __init__(self, handle):
        self.handle = handle

    def read(self):
        array = []
        for line in self.handle:
            array.append(line.rstrip('\n').lstrip().rstrip())
        self.handle.close()
        return array
