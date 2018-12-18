class Saver(object):
    def __init__(self, handle):
        self.handle = handle

    def save(self, line):
        self.handle.write(line+ "\n")
        return False
    def close(self):
        self.handle.close()
