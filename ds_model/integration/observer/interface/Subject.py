from __future__                     import annotations
from abc                            import ABC, abstractmethod
import integration.observer.interface.Observer as Observer

# абстрактный интерфейс для всех издателей событий
class Subject(ABC):

    @abstractmethod
    def attach(self,observer:Observer) -> None:
        pass

    @abstractmethod
    def detach(self,observer:Observer) -> None:
        pass

    @abstractmethod
    def notify(self) -> None:
        pass

