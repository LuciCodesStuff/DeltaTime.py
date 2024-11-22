import time

NANOSECOND = 0.000000001 # Be the timelord you've always wanted to be!

class DeltaTime:
    def __init__(self):
        self.last_ns = time.monotonic_ns()
        self.delta = (self.last_ns - time.monotonic_ns()) * NANOSECOND
    def run(self):
        ns = time.monotonic_ns()
        self.delta = (ns - self.last_ns) * NANOSECOND
        self.last_ns = ns
        return self.delta
