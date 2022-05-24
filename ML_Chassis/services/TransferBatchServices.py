import pandas as pd

class TransferBatchServices():
    def transfer(self,JsonBatch):
        transponentData = {}
        for line in JsonBatch['content']:
            for row in line['fields']:
                fieldName = row['field_name']
                fieldVal = row['field_val']
                if fieldName not in transponentData:
                    transponentData[fieldName] = []
                else:
                    transponentData[fieldName] = fieldVal
        return pd.DataFrame(data=transponentData)