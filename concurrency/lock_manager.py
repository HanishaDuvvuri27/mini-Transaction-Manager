from threading import RLock
from collections import defaultdict

class LockManager:
    def __init__(self):
        self.locks = defaultdict(RLock)

    def acquire(self, key):
        self.locks[key].acquire()

    def release(self, key):
        self.locks[key].release()
