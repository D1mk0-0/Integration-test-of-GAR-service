import pytest

from methods.base_method import BaseMethod
from data.address_data import AddressData
from methods.address_data_method import AddressDataMethod

#from spellchecker import SpellChecker <-- Для проверки орфографии ответов (Пока неактивно)

class TestContractApi():
    #@pytest.fixture(
    #    autouse=True,
    #    params=list(range(AddressDataMethod.len_line_json(AddressDataMethod)))
    #)
    #def setup(self, request):
    #    address_data = AddressDataMethod(line=2)
    #    address_data.suit(request.param)
    #    req = address_data.len_line_json()
    #    print(req)
    #    yield

    @pytest.mark.parametrize(
       argnames=['address'],
       argvalues=AddressData.address_base_set
    )
    def test_should_be_api_address_contract(self, address):
        self.response = BaseMethod(address)
        self.response.send_get_request_with_address(address, 10)
        self.response.should_be_status_code_200()
        self.response.should_be_quality_index()

    if __name__ == "__main__":
        pytest.main([__file__])
