class Env:
    def __init__(self):
        
        self.URL = "https://captive.apple.com/"
        self.regex = '<HTML><HEAD><TITLE>Success</TITLE></HEAD><BODY>Success</BODY></HTML>$'

        self.timeout = 8
        self.number_of_threads = 100

    def getURL(self):
        return self.URL

    def getRegex(self):
        return self.regex

    def getTimeout(self):
        return self.timeout

    def getNumberOfThreads(self):
        return self.number_of_threads

    def getAll(self):
        return {"number_of_threads":self.number_of_threads,"url":self.URL, "regex": self.regex, "timeout": self.timeout}
