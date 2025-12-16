from threading import Lock

class DataStore:
    def __init__(self):
        self._data = {}
        self._lock = Lock()

    def read(self, key):
        with self._lock:
            return self._data.get(key)

    def write(self, key, value):
        with self._lock:
            self._data[key] = value

    def delete(self, key):
        with self._lock:
            self._data.pop(key, None)

    def snapshot(self):
        with self._lock:
            return dict(self._data)
