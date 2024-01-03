import pytest
import random

from methods.base_method import BaseMethod as BM
from methods.contract_method import ContractMethod as CM
from data.negative_data import NegativeData as ND
from data.inspected_data import InspectedAddressValue as IAV

@pytest.mark.answer_structure
def test_should_be_correct_answer_structure(api_client):
    print('\nСтарт теста структуры корректного ответа..')
    answer_structure = BM(api_client)
    request = answer_structure \
        .send_get_request_with_address(
            IAV.INSPECTED_ADDRESS_VALUE, 5
    )
    answer_structure = BM(request)
    answer_structure.should_be_status_code_200()
    answer_structure = CM(request)
    answer_structure.validate_response_is_json()
    answer_structure.validation_json_in_response(IAV.INSPECTING_ADDRESS_PATTERN)
    print('Завершение теста.')

@pytest.mark.error_404
def test_should_be_404_error(api_client):
    print('\nСтарт теста ошибки 404..')
    non_existent_address = BM(api_client)
    request = non_existent_address \
        .send_get_request_with_address(
        IAV.NON_EXISTENT_ADDRESS, 5
    )
    non_existent_address = BM(request)
    non_existent_address.should_be_status_code_404()
    print('Завершение теста.')

@pytest.mark.error_400
@pytest.mark.parametrize('name, limit', ND.negative_data(ND))
def test_should_be_400_error(api_client, name, limit):
    print('\nСтарт теста ошибки 400..')
    print(f'Вариант неправильного запроса "name" : {name}. "limit" : {limit}')
    incorrect_request = BM(api_client)
    request = incorrect_request \
        .send_get_request_with_address(name, limit)
    incorrect_request = BM(request)
    incorrect_request.should_be_status_code_400()
    print('Завершение теста.')

@pytest.mark.correct_limit
@pytest.mark.parametrize('limit', [random.randint(1, 20) for _ in range(5)])
def test_should_be_correct_amount_limit(limit, api_client):
    print('\nСтарт теста возвращаемого значения limit..')
    correct_limit = BM(api_client)
    request = correct_limit \
        .send_get_request_with_address('Москва', limit)
    correct_limit = CM(request)
    correct_limit.should_be_hints_equal_to_limit(limit)
    print('Завершение теста.')




