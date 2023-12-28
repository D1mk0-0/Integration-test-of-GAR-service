import json

import pytest

class AddressDataMethod():

    ADDRESS_DATA_FILE_PATH = './data/address_data.json'

    def get_json_keys(self):
        with open(self.ADDRESS_DATA_FILE_PATH, 'r', encoding="utf-8") as file:
            data = json.load(file)
            keys = list(data.keys())
            return keys



