import pytest
import json

from methods.base_method import BaseMethod
from data.address_data import AddressData
from methods.address_data_method import AddressDataMethod

#from spellchecker import SpellChecker <-- Для проверки орфографии ответов (Пока неактивно)

#@pytest.mark.parametrize(
#    argnames=['address'],
#    argvalues=AddressData.address_base_set
#)

class TestContractApi():
    @pytest.fixture(scope='function', autouse=True)
    def setup(self):
        address_json = AddressDataMethod()
        address_json.get_json_keys()
        request = address_json
        address_set.append(request)

    @pytest.mark.parametrize('address', AddressDataMethod.get_json_keys())
    def test_should_be_api_address_contract(self, address):

        request = BaseMethod(address)
        request.send_get_request_with_address(address, 10)
        request.should_be_status_code_200()
        request.should_be_quality_index()

    if __name__ == "__main__":
        pytest.main([__file__])
