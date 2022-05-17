from typing                                     import List
from integration.observer.interface.Subject     import Subject
from integration.observer.interface.Observer    import Observer
from pyhive                                     import hive

class messageSubject(Subject):

    _observers: List[Observer] = []
    _state = None

    def __init__(self):
        pass

    def attach(self, observer: Observer) -> None:
        print(f'регистрация нового слушателя потока сообщений кафка {observer}')
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        print(f'удаление слушателя {observer}')
        self._observers.remove(observer)

    def notify(self) -> None:
        for observer in self._observers:
            observer.update(self)

    def businesFunction(self) -> None:
        print('слушаем какой нибудь топик')