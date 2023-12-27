import pytest

from methods.base_method import BaseMethod
from data.address_data import AddressData

#from spellchecker import SpellChecker <-- Для проверки орфографии ответов (Пока неактивно)

@pytest.mark.parametrize(
    argnames=['address'],
    argvalues=AddressData.address_base_set
)
def test_should_be_api_address_contract(address):
    if address == 'город М':
        pytest.xfail(f'Слишком уж некорректный адрес: {address}')
        return
    request = BaseMethod(address)
    request.send_get_request_with_address(address, 10)
    request.should_be_status_code_200()
    request.should_be_quality_index()

if __name__ == "__main__":
    pytest.main([__file__])
