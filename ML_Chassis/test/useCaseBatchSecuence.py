import unittest
from services import BatchService

class TestBatchServices(unittest.TestCase):

    def setUp(self) -> None:
        self.batcherServices = BatchService()

    def test_getBatch(self):
        print('')
        print('тест на получение пачки')
        self.batcherServices.requestBatch()
        print('Пачка получена моделью')

    def test_saveBatch(self):
        print('')
        print('тест на сохранение пачки')
        print('целевые переменные вычеслены')
        self.batcherServices.saveBatch()

if __name__ == "__main__":
  unittest.main()