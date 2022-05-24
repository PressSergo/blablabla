from infrastructure import IBatchSource

class BatchRepository():
    _batchSource: IBatchSource = None

    def __init__(self,source: IBatchSource) -> None:
        self._batchSource = source

    def requestBatch(self):
        pass

    def saveBatch(self):
        print('сохраняем пачку')


    def changeStateBatch(self):
        print('изменям состояние пачки')

    def determinationBatch(self):
        pass

