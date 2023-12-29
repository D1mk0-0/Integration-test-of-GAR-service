import pytest

from methods.base_method import BaseMethod
from data.address_data import AddressData
from methods.address_data_method import AddressDataMethod

#from spellchecker import SpellChecker <-- Для проверки орфографии ответов (Пока неактивно)

#@pytest.mark.parametrize(
#    argnames=['address'],
#    argvalues=AddressData.address_base_set
#)

class TestContractApi():
    #@pytest.fixture(scope='function', autouse=True)
    #def setup(self):
    #    test_data = AddressDataMethod.get_json_keys()
    #    global

    @pytest.mark.parametrize(
       argnames=['address'],
       argvalues=AddressData.address_base_set
    )
    def test_should_be_api_address_contract(self, address):
        self.response = BaseMethod(address)
        self.response.send_get_request_with_address(address, 10)
        self.response.should_be_status_code_200()
        self.response.should_be_quality_index()
        address_data = AddressDataMethod(address)
        result = address_data.get_address_response(0)
        print(result)

    if __name__ == "__main__":
        pytest.main([__file__])
