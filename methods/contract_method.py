import requests
from .base_method import BaseMethod

class ContractMethod(BaseMethod):

    def __init__(self, response):
        super().__init__(response)

    def should_be_response_according_to_the_contract(self):
        self.should_be_json_response()

    def should_be_json_response(self):
        self.response = requests.get(self.address)
        json_data = self.response.json()
        assert isinstance(json_data, dict), \
            'В ответе нет json-файла'
