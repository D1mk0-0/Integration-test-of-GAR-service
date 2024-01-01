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

    def count_matching_items(self, list1, list2):
        return len(set(list1).intersection(list2))

    def should_be_quality_index(self, request):
        response_json = request.json()
        response_first_hint = response_json[0]['name']['default']
        list_address = request.split()
        list_response_address = response_first_hint.split()
        first_hint_quality_index = self.count_matching_items(list_address, list_response_address)
        assert first_hint_quality_index >= 2, \
            f'Для запроса: "{request}" - слишком низкий индекс качества первой подсказки = {first_hint_quality_index}. ' \
            f'Была возвращена подсказка: {response_first_hint}'


