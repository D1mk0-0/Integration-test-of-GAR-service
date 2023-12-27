
class BaseMethod():
    def __init__(self, response):
        self.response = response

    def get_address_from_json(self):
        address = self.response.json()
        address.response_json[0]['name']['default']
        return address

    def should_be_status_code_200(self):
        assert self.response.status_code == 200, \
            f'\nСтатус ответа не в порядке :{self.response.status_code}'

