import time 

class BenchmarkEngine:
    def __init__(self):
        self.reset()
        
    def begin(self):
        self.startTime = time.time()

    def end(self):
        self.endTime = time.time()
        self.duration = self.endTime - self.startTime

    def reset(self):
        self.startTime = None
        self.endRime = None
        self.duration = None
