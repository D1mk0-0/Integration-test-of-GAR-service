import pytest
import random

from methods.base_method import BaseMethod as BM
from methods.contract_method import ContractMethod as CM
from data.address_data import AddressData as AD

#from spellchecker import SpellChecker <-- Для проверки орфографии ответов (Пока неактивно)

@pytest.mark.answer_structure
def test_should_be_correct_answer_structure(prepared_data):
    print('\nСтарт теста структуры корректного ответа..')
    answer_structure = BM(prepared_data)
    answer_structure.should_be_status_code_200()
    answer_structure = CM(prepared_data)
    answer_structure.validate_response_is_json()
    answer_structure.validation_json_in_response()
    print('Завершение теста.')

@pytest.mark.error_404
def test_should_be_404_error(prepared_data_404):
    print('\nСтарт теста ошибки 404..')
    non_existent_address = BM(prepared_data_404)
    non_existent_address.should_be_status_code_404()
    print('Завершение теста.')

@pytest.mark.error_400
@pytest.mark.parametrize('name, limit', AD.negative_data(AD))
def test_should_be_400_error(api_client, name, limit):
    print('\nСтарт теста ошибки 400..')
    print(f'Вариант неправильного запроса "name" : {name}. "limit" : {limit}')
    incorrect_requests = BM(api_client)
    request = incorrect_requests \
        .send_get_request_with_address(name, limit)
    incorrect_request = BM(request)
    incorrect_request.should_be_status_code_400()
    print('Завершение теста.')

@pytest.mark.correct_limit
@pytest.mark.parametrize('limit', [random.randint(1, 20) for _ in range(5)])
def test_should_be_correct_amount_limit(limit, api_client):
    print('\nСтарт теста возвращаемого значения limit..')
    print(f'limit в запросе установлен: {limit}')
    correct_limit = BM(api_client)
    request = correct_limit \
        .send_get_request_with_address('Москва', limit)




