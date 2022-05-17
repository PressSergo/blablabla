from integration.jobs.statePackage.statePackage import StatePackage
import pandas as pd

def hiveStateLoadData(connection,notify,self):
    print(f'Ждем подходящего состояния пакета unif_dm_package_condition')
    hiveCursor = connection.cursor()
    hiveCursor.execute('select * from unif_dm_package_condition order by condidtion_datetime desc limit 1')
    packageInfo = hiveCursor.fetchall()
    print(packageInfo)
    statePackage = packageInfo[0][3] # хард поправить
    if statePackage == 2:
        try:
            print('стартуем процесс обогощения пачки')
            preparePandasDataFrame(connection,packageInfo[0],self)
            notify()
            try:
                hiveSetState(hiveCursor, packageInfo[0], state=3)
            except:
                pass
            saveTargetValue(hiveCursor,packageInfo[0],'обогащен')
        except:
            hiveCursor.close()
    hiveCursor.close()


# для пакета нужен хеш чтобы отслеживать актуальность пакета в случае быстрых таймаутов
def hiveSetState(hiveCursor,packageInfo,state):
    print('пачка обогатилась меняем состояние')
    hiveCursor.execute(f"insert into table unif_dm_package_condition values ({packageInfo[0]},{packageInfo[1]},CURRENT_TIMESTAMP,{state},'фичи подготовлены')")
    hiveCursor.fetchAll()

def preparePandasDataFrame(hiveConnection,packageInfo,self):
    dataframe = pd.read_sql(f"select * from data_package where  data_package.package_id = {packageInfo[0]}",hiveConnection)
    self._state = dataframe

def saveTargetValue(hiveCursor,packageInfo,targetData):
    print('сохраняем целевую перменную')
    hiveCursor.execute(f"insert into table data_package values ({packageInfo[0]},'3','1','21',{targetData})")
    hiveCursor.fetchAll()