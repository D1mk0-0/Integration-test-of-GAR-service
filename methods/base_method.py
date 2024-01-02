import requests

from .connect_method import ConnectMethod as CM

class BaseMethod():
    def __init__(self, prepared_data):
        self.prepared_data = prepared_data

    def send_get_request_with_address(self, name, limit):
       payload = {'Name': f'{name}', 'Limit': f'{limit}'}
       response = requests.get(f'{CM.BASE_URL}{CM.GET_URL_ADDRESS}', params=payload)
       return response

    def should_be_status_code_200(self):
        assert self.prepared_data.status_code == 200, \
            f'Статус ответа не в порядке :{self.prepared_data.status_code}'
        print('Статус ответа в порядке 200')

    def should_be_status_code_400(self):
        assert self.prepared_data.status_code == 400, \
            f'Статус ответа не в порядке :{self.prepared_data.status_code}. В этом тесте ожидалось 400'
        print('Статус ответа в порядке 400 (в этом тесте так и должно быть)')

    def should_be_status_code_404(self):
        assert self.prepared_data.status_code == 404, \
            f'Статус ответа не в порядке :{self.prepared_data.status_code}. В этом тесте ожидалось 404'
        print('Статус ответа в порядке 404 (в этом тесте так и должно быть)')



