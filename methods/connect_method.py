from .base_method import BaseMethod

class ConnectMethod(BaseMethod):
    BASE_URL = 'http://gar.gblinov.ru:18181'
    GET_URL_ADDRESS = '/v1/Addresses'

    #Красная ссылка
    GET_URL_ID = '/v1/Addresses/{id}'
