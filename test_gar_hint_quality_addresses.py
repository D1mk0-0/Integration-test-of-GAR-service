import pytest

from methods.base_method import BaseMethod as BM
from methods.address_data_method import AddressDataMethod as ADM

@pytest.mark.hint_quality
@pytest.mark.parametrize('address_sent, address_expected',
                         ADM.get_key_value_pairs_from_json(
                             ADM, 'data/address_data.json'
                         ))
def test_hint_quality(api_client, address_sent, address_expected):
    print('\nСтарт теста качества подсказки..')
    hint_quality = BM(api_client)
    request = hint_quality \
        .send_get_request_with_address(address_sent, 5)
    hint_quality = BM(request)
    hint_quality.should_be_status_code_200()
    hint_quality = ADM(request)
    hint_quality.validation_name_field_in_response(address_sent ,address_expected)
    print('Завершение теста.')
