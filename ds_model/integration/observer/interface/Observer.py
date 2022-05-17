from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List
import integration.observer.interface.Subject as Subject


#Общий интерфейс для всех наблюдателей
class Observer():

    @abstractmethod
    def update(self, subject: Subject) -> None:
        pass