import json

class AddressDataMethod():

    def __init__(self, line):
        self.line = line

    # Путь к json указан относительно места вызова этой функции (test_gar_api_contract.py)
    def get_json_line(self, line):
        with open('data/address_data.json', 'r', encoding="UTF-8") as file:
            data = json.load(file)
            keys_list = list(data.keys())
            value_list = list(data.values())
            return keys_list[line], value_list[line]

    def get_address_response(self, line):
        json_line = self.get_json_line(line)
        address_response = json_line[0]
        return address_response

    def get_address_hint(self, line):
        json_line = self.get_json_line(line)
        address_hint = json_line[1]
        return address_hint

    def suit(self, line):
        print(self.get_address_response(line))
        print(self.get_address_hint(line))



