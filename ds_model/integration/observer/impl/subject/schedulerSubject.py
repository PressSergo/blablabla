from typing                                     import List

from integration.jobs.HiveStateLoadData import hiveStateLoadData
from integration.observer.interface.Subject     import Subject
from integration.observer.interface.Observer    import Observer
from threading                                  import Thread
import schedule
import time
from pyhive                                     import hive
import pandas as pd

class schedulerSubject(Subject):

    _observers: List[Observer] = []
    _state = None

    def __init__(self):
        self.hiveconn = hive.Connection(host='localhost', port=10000, database='ds_databse')

    def attach(self, observer: Observer) -> None:
        print(f'регистрация нового слушателя по расписанию {observer}')
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        print(f'удаление слушателя {observer}')
        self._observers.remove(observer)

    def notify(self) -> None:
        for observer in self._observers:
            observer.update(self)

    def businesFunction(self) -> None:
        def wrapper():
            schedule.every(5).seconds.do(lambda :hiveStateLoadData(self.hiveconn,self.notify,self))
            while True:
                schedule.run_pending()
                time.sleep(1) # каждую секунду делает опрос

        Thread(target=wrapper).start()
