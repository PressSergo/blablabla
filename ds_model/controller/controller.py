from flask import Blueprint

settlement_api = Blueprint('settlement_api',__name__)

@settlement_api.route('/api/getSimpleData',methods=['GET'])
def simpleGetData():
    return 'simple get'