import json

class BatchSpecification():
    _specificationSource = None

    def __init__(self) -> None:
        self._specificationSource = json.load(open('../resources/batchSpec.json'))

    def isSatisfied(self,batch):
        for i in self._specificationSource['required']:
            if i not in batch:
                return False
        return True
