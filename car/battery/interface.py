import abc
from datetime import datetime
class Battery(metaclass=abc.ABCMeta):
    current_date = datetime.now().date()
    @abc.abstractmethod
    def needs_service(self):
        pass