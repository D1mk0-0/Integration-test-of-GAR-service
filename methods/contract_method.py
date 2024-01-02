import json
import jsonschema
from jsonschema import validate

from .base_method import BaseMethod

class ContractMethod(BaseMethod):

    def __init__(self, prepared_data):
        self.prepared_data = prepared_data

    def validate_response_is_json(self):
        json_data = self.prepared_data.json()
        assert isinstance(json_data, list), \
            'Ответ не содержит JSON-объект'
        print('Ответ содержит JSON-объект')

    def validation_json_in_response(self, schema):
        data = self.prepared_data.json()
        try:
            validate(
                instance=data,
                schema=schema
            )
            print('Все элементы JSON-объекта вернулись и заполнены верно')
        except jsonschema.exceptions.ValidationError as e:
            assert False, f'В JSON-объекте был возвращен некорректный элемент : {e}'

    def should_be_hints_equal_to_limit(self, limit):
        json_response = self.prepared_data.json()
        name_count = sum(1 for item in json_response if 'name' in item)
        assert limit == name_count, \
            f'Количество возвращенных подсказок ({name_count}), отличается от значения limit ({limit})'
        print(f'Количество возвращенных подсказок ({name_count}) равно limit ({limit})')




