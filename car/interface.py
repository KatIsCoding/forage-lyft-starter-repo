import abc
from .engine import Engine
from .battery import Battery

class Car(metaclass=abc.ABCMeta):
    engine: Engine
    battery: Battery
    @abc.abstractmethod
    def needs_service(self):
      pass