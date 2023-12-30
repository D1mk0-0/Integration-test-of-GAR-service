import pytest
import requests

from methods.connect_method import ConnectMethod
from methods.address_data_method import AddressDataMethod

@pytest.fixture
def prepared_data():
    limit = 5
    address = 'г. Москва, ш. Можайское, 45,4,3'
    payload = {'Name': f'{address}', 'Limit': f'{limit}'}
    response = requests.get(f'{ConnectMethod.BASE_URL}{ConnectMethod.GET_URL_ADDRESS}', params=payload)
    return response