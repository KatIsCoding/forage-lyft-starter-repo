import abc

class Engine(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def needs_service(self):
        pass