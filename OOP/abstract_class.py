# must have at least one abstract method
# cannot be instantiated
from abc import ABC, abstractmethod


# creates a class that has ABCMeta as a metaclass(creates classes)
class Log(ABC):  # same as: class Log(metaclass=ABCMeta):

    @abstractmethod
    def _log(self, msg): ...

    def log_error(self, msg):
        return self._log(f'Error: {msg}')

    def log_success(self, msg):
        return self._log(f'Success: {msg}')


class LogPrintMixin(Log):
    def _log(self, msg):
        print(f'{msg} ({self.__class__.__name__})')


l = LogPrintMixin()
l.log_error("___")
