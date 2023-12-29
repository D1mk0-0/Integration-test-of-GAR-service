import pytest

from methods.base_method import BaseMethod
from methods.address_data_method import AddressDataMethod

#from spellchecker import SpellChecker <-- Для проверки орфографии ответов (Пока неактивно)

class TestGarApiContract():
    @pytest.mark.parametrize('address', AddressDataMethod.get_json_keys(AddressDataMethod))
    def test_should_be_api_address_contract(self, address):
        self.response = BaseMethod(address)
        self.response.send_get_request_with_address(address, 10)
        self.response.should_be_status_code_200()
        self.response.should_be_quality_index()

    if __name__ == "__main__":
        pytest.main([__file__])
