from integration.observer.impl.subject.schedulerSubject import schedulerSubject
from integration.observer.impl.subject.messageSubject import messageSubject
from integration.observer.impl.observer.Bancrut import BancrutObserver

#Создание издателей
scheduleSubject = schedulerSubject()
messageSubject = messageSubject()

#Создание подписчиков
bancrutObserver = BancrutObserver()


#Регистрация всего на свете
scheduleSubject.attach(observer = bancrutObserver)
messageSubject.attach(observer = bancrutObserver)

#Запуск и прочие настройки
scheduleSubject.businesFunction()
messageSubject.businesFunction()