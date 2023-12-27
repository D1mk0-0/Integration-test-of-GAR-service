import requests

class BaseMethod():
    def __init__(self, response, address):
        self.response = response
        self.address = address

    def get_address_from_json(self):
        address = self.response.json()
        address.response_json[0]['name']['default']
        return address

    def should_be_status_code_200(self):
        assert self.response.status_code == 200, \
            f'\nСтатус ответа не в порядке :{self.response.status_code}'

    def count_matching_items(self, list1, list2):
        return len(set(list1).intersection(list2))

    def should_be_quality_index(self):
        response_json = self.response.json()
        response_address = response_json[0]['name']['default']
        list_address = self.address.split()
        list_response_address = response_address.split()
        hint_quality_index = self.count_matching_items(list_address, list_response_address)
        assert hint_quality_index >= 2, \
            f'Для запроса: "{self.address}" - слишком низкий индекс качества подсказки = {hint_quality_index}. ' \
            f'Была возвращена подсказка: {response_address}'






