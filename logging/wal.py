import json
import os
from threading import Lock

class WriteAheadLog:
    def __init__(self, filename="wal.log"):
        self.filename = filename
        self._lock = Lock()

    def append(self, record: dict):
        with self._lock, open(self.filename, "a") as f:
            f.write(json.dumps(record) + "\n")
            f.flush()
            os.fsync(f.fileno())

    def read_all(self):
        if not os.path.exists(self.filename):
            return []
        with open(self.filename) as f:
            return [json.loads(line) for line in f]

    def clear(self):
        open(self.filename, "w").close()
