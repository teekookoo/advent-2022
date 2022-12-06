import time

def chunksof(n, iterable):
    it = iter(iterable)
    temp = [x for x in range(n)]
    for i, x in enumerate(it):
        temp[i % n] = x
        if (i + 1) % n == 0:
            yield tuple(temp)
    
    assert (i + 1) % n == 0

class Stopwatch:
    def __init__(self):
        self.__times = []
    
    def start(self):
        self.__times = [time.perf_counter_ns()]
    
    def add_split(self):
        self.__times.append(time.perf_counter_ns())
    
    def stop(self, add_split=True):
        if add_split:
            self.add_split()
        
        return [t - self.__times[0] for t in self.__times]