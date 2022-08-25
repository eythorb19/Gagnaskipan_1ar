import time 
#Verkefni 1 - tími 1
#timeit fall

class Timer():
    def __init__(self):
        self.start_time = None
        self.lap = list

    def __str__(self):
        return f'end_time({self.elapsed})'

    def start(self):
        self.start_time = time.time()
        return self.start_time
        
    def stop(self):
        self.end_time = time.time()
        return self.end_time

    def elapsed(self):
        '''Time in seconds'''

        self.end_time = self.stop()
        elapsed_time = self.end_time - self.start_time
        return elapsed_time
        