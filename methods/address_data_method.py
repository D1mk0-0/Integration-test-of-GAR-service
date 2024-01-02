import json

class AddressDataMethod():

    def __init__(self, prepared_data):
        self.prepared_data = prepared_data

    def get_key_value_pairs_from_json(self, json_file):
        with open(json_file, 'r', encoding="UTF-8") as file:
            data = json.load(file)
            key_value_pairs = [(key, value) for key, value in data.items()]
            return key_value_pairs

    def validation_name_field_in_response(self, address_sent, address_expected):
       data = self.prepared_data.json()
       expected_value = list(data)[0]['name']['default']
       assert expected_value == address_expected, \
           '\nПервая подсказка отличается от ожидаемой:' \
           f'\nОтправлен адресс : {address_sent}' \
           f'\nВернулась подсказка : {expected_value}' \
           f'\nОжидаемая подсказка : {address_expected}'
       print('Первая подсказка возвращена верно')