from abc import ABC, abstractmethod

class Subject:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Subject, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        self._observers = []

    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

    def notify(self, **kwargs):
        for observer in self._observers:
            observer.update(self, **kwargs)

class Observer(ABC):
    @abstractmethod
    def update(self, subject, **kwargs):
        pass
