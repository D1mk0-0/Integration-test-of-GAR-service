import requests
import pytest

from methods.base_method import BaseMethod
from methods.connect_method import ConnectMethod
from data.address_data import AddressData

#from spellchecker import SpellChecker <-- Для проверки орфографии ответов (Пока неактивно)


def count_matching_items(list1, list2):
    return len(set(list1).intersection(list2))

@pytest.mark.parametrize(
    argnames=['address'],
    argvalues=AddressData.address_base_set
)
def test_should_be_api_address_contract(address):
    if address == 'город М':
        pytest.xfail(f'Слишком уж некорректный адрес: {address}')
        return
    payload = {'Name': f'{address}', 'Limit': '10'}
    response = requests.get(f'{ConnectMethod.BASE_URL}{ConnectMethod.GET_URL_ADDRESS}', params=payload)
    request = BaseMethod(response, address)
    request.should_be_status_code_200()
    request.should_be_quality_index()
    #assert response_address == re.compile(r"г\s*(\w+),\s*ул\s*(\w+),\s*д\.\s*(\d+)\s*кв\s*(\d+)"), \
    #    f'{response_address} не соответствует формату ответа.'

if __name__ == "__main__":
    pytest.main([__file__])
