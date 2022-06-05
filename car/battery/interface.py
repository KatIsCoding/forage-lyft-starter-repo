import abc
from datetime import datetime
class Battery(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def needs_service(self):
        pass