from abc import ABC,abstractmethod

class IBatchSource(ABC):

    @abstractmethod
    def execute(self):
        pass