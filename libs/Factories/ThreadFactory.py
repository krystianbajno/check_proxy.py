from threading import Thread

class ThreadFactory(object):
    def __init__(self, job_reference, number_of_threads):
        self.job_reference = job_reference
        self.number_of_threads = number_of_threads

    def thread_method(self, *args):
        self.job_reference.run()

    def run(self):
        for n in range(0, self.number_of_threads):
            thread = Thread(target=self.thread_method)
            thread.daemon = True
            thread.start()