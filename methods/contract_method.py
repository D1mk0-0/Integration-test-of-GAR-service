import json

from .base_method import BaseMethod
from data.inspected_data import InspectedAddressValue as IAV

class ContractMethod(BaseMethod):

    def __init__(self, prepared_data):
        self.prepared_data = prepared_data

    def validate_response_is_json(self):
        json_data = self.prepared_data.json()
        assert isinstance(json_data, list), \
            "Ответ не содержит JSON-объект"
        print("Ответ содержит JSON-объект")

    def get_json_line(self, line):
        with open('../data/address_data.json', 'r', encoding="UTF-8") as file:
            data = json.load(file)
            keys_list = list(data.keys())
            value_list = list(data.values())
            return keys_list[line], value_list[line]

    def validation_name_field_in_response(self):
        data = self.prepared_data.json()
        expected_value = list(data)[0]['name']['default']
        assert expected_value == IAV.INSPECTING_ADDRESS_VALUE, \
            '\nНеверное значение ключа "default" в ответе: ' \
            f'\nОжидаемое значение: {IAV.INSPECTING_ADDRESS_VALUE}' \
            f'\nФактческое значение: {expected_value}'
        print('Ключ "default" в ответе заполнен верно')
        #return keys_list, value_list


        #required_keys_values = self.prepared_data.json()
        #required_keys_values = ['key1', 'key2', 'key3']  # Список требуемых ключей

        #if not isinstance(required_keys_values, list):
        #    raise ValueError("JSON data is not a valid object")
#
        #for key in required_keys_values:
        #    if key not in required_keys_values:
        #        raise ValueError(f"Key '{key}' is missing in the JSON data")
#
        ## Дополнительные проверки значений ключей или их типов могут быть добавлены здесь
#
        #print("JSON data is valid")


