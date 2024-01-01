import pytest

from methods.base_method import BaseMethod
from methods.address_data_method import AddressDataMethod
from methods.contract_method import ContractMethod

#from spellchecker import SpellChecker <-- Для проверки орфографии ответов (Пока неактивно)

@pytest.mark.answer_structure
def test_correct_answer_structure(prepared_data):
    print('\nСтарт теста структуры корректного ответа..')
    answer_structure = BaseMethod(prepared_data)
    answer_structure.should_be_status_code_200()
    answer_structure = ContractMethod(prepared_data)
    answer_structure.validate_response_is_json()
    answer_structure.validation_json_in_response()
    print('Завершение теста.')

@pytest.mark.error_404
def test_404_error(prepared_data):
    print('\nСтарт теста ошибки 404..')


#if __name__ == "__main__":
#    pytest.main([__file__])


