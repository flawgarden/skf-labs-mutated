from typing import TypeVar, Generic
from threading import Lock

S = TypeVar('S')


class Wrapper(Generic[S]):
    i: S
    lock: Lock

    def __init__(self, t: S):
        self.i = t
        self.lock = Lock()


from threading import Thread

class SettingTask(Thread):
    _w: Wrapper[str]
    _s: str

    def __init__(self, w: Wrapper, s: str):
        super().__init__()
        self._w = w
        self._s = s

    def run(self):
        self._w.i = self._s


from threading import Thread

class SwitchingTask(Thread):
    _w: Wrapper[str]
    _s: str

    def __init__(self, w: Wrapper, s: str):
        super().__init__()
        self._w = w
        self._s = s

    def run(self):
        with self._w.lock:
            if self._w.i == "":
                self._w.i = self._s
            else:
                self._w.i = ""


from threading import RLock, Condition


class NullAndRestore:
    _s: str | None
    _original: str
    _lock: RLock
    _set_to_none: Condition

    def __init__(self, s):
        self._s = s
        self._original = s
        self._lock = RLock()
        self._set_to_none = Condition(self._lock)

    def null_method(self):
        self._lock.acquire()
        self._s = None
        self._set_to_none.notify_all()
        self._lock.release()

    def restore(self):
        self._lock.acquire()
        while self._s is not None:
            try:
                self._set_to_none.wait()
            except RuntimeError:
                raise
        self._s = self._original
        self._lock.release()

    def get(self) -> str | None:
        ret = None
        self._lock.acquire()
        ret = self._s
        self._lock.release()
        return ret