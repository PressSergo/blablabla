from infrastructure import IBatchSource

class ModelRepository():
    _batchSource: IBatchSource = None

    def __init__(self,source: IBatchSource) -> None:
        self._batchSource = source

    def addModel(self):
        pass

    def deleteModel(self):
        pass

    def loadModel(self):
        return self._batchSource.execute()

    def loadAllModel(self):
        pass