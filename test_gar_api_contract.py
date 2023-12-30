import pytest

from methods.base_method import BaseMethod
from methods.address_data_method import AddressDataMethod
from methods.contract_method import ContractMethod

#from spellchecker import SpellChecker <-- Для проверки орфографии ответов (Пока неактивно)

def test_correct_answer_structure(prepared_data):
    answer_structure = BaseMethod(prepared_data)
    answer_structure.should_be_status_code_200()



class TestGarApiContract():





    #"@pytest.mark.parametrize('address', AddressDataMethod.get_json_keys(AddressDataMethod))
    #def test_correct_answer_structure(self, address):
    #    self.response = BaseMethod(address)
    #    self.response.send_get_request_with_address(address, 10)
    #    self.response.should_be_status_code_200()
    #    self.response.should_be_quality_index()
    #    self.contract = ContractMethod()
    #    self.contract.should_be_json_response()

    if __name__ == "__main__":
        pytest.main([__file__])
