import requests

from .connect_method import ConnectMethod

class BaseMethod():
    def __init__(self, address):
        self.address = address

    def send_get_request_with_address(self, address, limit):
        payload = {'Name': f'{address}', 'Limit': f'{limit}'}
        self.response = requests.get(f'{ConnectMethod.BASE_URL}{ConnectMethod.GET_URL_ADDRESS}', params=payload)
        return self.response

    def should_be_status_code_200(self):
        assert self.response.status_code == 200, \
            f'Статус ответа не в порядке :{self.response.status_code}'

    def count_matching_items(self, list1, list2):
        return len(set(list1).intersection(list2))

    def should_be_quality_index(self):
        response_json = self.response.json()
        response_first_hint = response_json[0]['name']['default']
        list_address = self.address.split()
        list_response_address = response_first_hint.split()
        first_hint_quality_index = self.count_matching_items(list_address, list_response_address)
        assert first_hint_quality_index >= 2, \
            f'Для запроса: "{self.address}" - слишком низкий индекс качества первой подсказки = {first_hint_quality_index}. ' \
            f'Была возвращена подсказка: {response_first_hint}'

    #def should_be_accordance_with_contract(self):


# assert response_address == re.compile(r"г\s*(\w+),\s*ул\s*(\w+),\s*д\.\s*(\d+)\s*кв\s*(\d+)"), \
#    f'{response_address} не соответствует формату ответа.'
