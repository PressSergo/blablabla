def saveTargetValueData(fun,**kwargs):
    def theWrapper():
        fun(kwargs['dataframe'])
        targetValue = kwargs['dataframe']
        print('запись целевой переменной')
        print(targetValue['data_package.package_id'])
    return theWrapper