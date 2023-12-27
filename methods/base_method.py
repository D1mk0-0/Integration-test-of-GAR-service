class BaseMethod():
    def __init__(self, response):
        self.response = response

    def get_address_from_json(self):
        self.address = self.response.json()
        self.address.response_json[0]['name']['default']
