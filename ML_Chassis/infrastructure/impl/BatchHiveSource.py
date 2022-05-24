from infrastructure import IBatchSource

class BatchHiveImpl(IBatchSource):
    def execute(self):
        return ['load model info']