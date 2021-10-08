
import threading


class TaskRunnerStub:
    def __init__(self):
        self.threads = []

    def run(self, method, arguments):
        method(*arguments)

    def listen(self):
        print("Stub finished")


class TaskRunner:
    def __init__(self):
        self.threads = []
        self.waiting = []
        self.runningThreads = 0

    def run(self, method, arguments):
        if (self.runningThreads < 10):
            self.runningThreads += 1
            thread = threading.Thread(target=method, args=arguments)
            thread.start()
            self.threads.append(thread)

    def listen(self):
        for thread in self.threads:
            thread.join()
