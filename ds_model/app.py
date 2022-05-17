from flask import Flask
from controller.controller import settlement_api
import integration
import py_eureka_client.eureka_client as eureka_client

rest_port = 8050
eureka_client.init(eureka_server="http://127.0.0.1:8761/eureka",
                   app_name="Bancrut",
                   instance_port=rest_port)

app = Flask(__name__)
app.register_blueprint(settlement_api)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port = rest_port)



# распределенный пандас dask (ОСИП выгрузка данных) https://docs.dask.org/en/stable/
# lifemanager thread java https://www.baeldung.com/java-thread-lifecycle
# java concurrent https://www.baeldung.com/java-util-concurrent  ScheduledExecutorService
# https://www.baeldung.com/java-jdbc-loading-drivers automatic discovery service, service provider discovery
# модель это микросервис
# decimal в gRPC, посмотреть за это
# характер взаимодейсвия посмотреть синхроность/асинхронность
# посмотреть на синхрон дизайнтайма/рантайма
# посмотреть мониторинг жизненный цикл (регистрация запуск слом и так далее)
# выглядит как наличие service discovery посмотреть как работает microservices chasis
# посмотреть за хеш пачки
# контентно ориентированная файловая система - посмотреть что такое (связка с гитом)
# верификация схемы для нормальной работы пандаса, в случае если что-то поменялось (иначе может сломаться все для pandas/json)
# https://json-schema.org/ добавочно к выше теме посмотреть
# https://github.com/jviotti/awesome-jsonschema аналогично для темы выше