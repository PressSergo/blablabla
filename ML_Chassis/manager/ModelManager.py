from manager        import ModelState
from specification  import ModelSpecification
from infrastructure import ModelRepository
from infrastructure import BatchHiveImpl

class ModelManager():
    _modelState: ModelState = ModelState
    _modelSpecification: ModelSpecification = ModelSpecification()
    _modelRepository: ModelRepository = ModelRepository(BatchHiveImpl())

    def registrationModel(self):
        pass

    def deRegistrationModel(self):
        pass

    def getModelInfo(self):
        return self._modelRepository.loadModel()
