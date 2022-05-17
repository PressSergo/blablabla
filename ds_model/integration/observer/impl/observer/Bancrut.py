from integration.observer.interface import Subject
from integration.observer.interface.Observer import Observer
from domain.BancrutModel.BancrutDsModel import BancrutPipline

class BancrutObserver(Observer):
    def update(self, subject: Subject) -> None:
        BancrutPipline(subject._state)