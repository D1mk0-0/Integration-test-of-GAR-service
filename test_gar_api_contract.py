import pytest
import requests

from .pages.address_page import AddressBase

class TestGarApiContract():

    address = (AddressBase.address)

    @pytest.mark.parametrize('address', address)
    def test_should_be_response_with_hint(self, address):
        BASE_URL = 'http://gar.gblinov.ru:18181/'
        data = {"address" : address}

        response = requests.get(BASE_URL)
        print(response.status_code)
        print(response.text)
