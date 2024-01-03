import pytest

from methods.base_method import BaseMethod as BM
from methods.contract_method import ContractMethod as CM
from data.inspected_data import InspectedAddressValue as IAV

@pytest.mark.id_structure
def test_should_be_address_details(api_client):
    print('Старт теста деталей адреса ID..')
    address_details = BM(api_client)
    request = address_details \
        .send_get_request_with_id('1403580')
    address_details = BM(request)
    address_details.should_be_status_code_200()
    address_details = CM(request)
    address_details.validation_json_in_response(IAV.INSPECTING_ID_PATTERN)
    print('Завершение теста.')
