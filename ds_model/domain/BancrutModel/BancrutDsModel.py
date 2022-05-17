from integration.decoratorPandas.decoratorPandas import saveTargetValueData

# @saveTargetValueData
def BancrutPipline(dataframe):
    prepareDataFrame(dataframe)
    anyActionModel(dataframe)


def prepareDataFrame(dataframe):
    print('Обработка пандаса')
    print(dataframe.columns)
    print(dataframe.shape)

def anyActionModel(dataframe):
    print('какие-то еще действия любые')


