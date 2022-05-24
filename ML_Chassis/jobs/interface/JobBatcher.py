from abc import ABC, abstractmethod

class JobBatcher(ABC):

    @abstractmethod
    def execute(self):
        print('асинхронно выполняем задачу')
