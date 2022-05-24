from services       import BatchState
from services       import TransferBatchServices
from specification  import BatchSpecification
from infrastructure import BatchRepository
from infrastructure import BatchHiveImpl
from manager        import ModelManager
from jobs           import CronJob
from jobs           import JobBatcher

class BatchService():
    _batchState = None
    _transferBatchService: TransferBatchServices = None
    _batchSpecification: BatchSpecification = None
    _batchRepository: BatchRepository = None
    _modelManager: ModelManager = ModelManager()
    _jobBatcher: JobBatcher = None

    def __init__(self) -> None:
        self._batchState = BatchState
        self._transferBatchService = TransferBatchServices()
        self._batchSpecification = BatchSpecification()
        self._batchRepository = BatchRepository(BatchHiveImpl())
        self._jobBatcher = CronJob()

    def requestBatch(self):
        print('Получаем информацию о модели')
        modelInfo = self._modelManager.getModelInfo()
        print('начинаем ассинхронную загрузку пачки')
        batch = self._jobBatcher.execute()
        print('Пачка загружена')
        if self._batchSpecification.isSatisfied(batch):
            print('возвращаем пачку в виде пандаса')
            return self._transferBatchService.transfer(batch)
        else:
            print('По итогу тут ошибка, продумать обработчик ошибок')
            return None



    def reRequestBatch(self):
        pass

    def saveBatch(self):
        print('вызов сохранения пачки')
        self.changeStateBatch()
        self._batchRepository.saveBatch()
        print('пачка сохранена')

    def determBatch(self):
        pass

    def changeStateBatch(self):
        self._batchRepository.changeStateBatch()