import pytest
import requests

from methods.connect_method import ConnectMethod as CM
from data.inspected_data import InspectedAddressValue as IAV


@pytest.fixture
def prepared_data():
    limit = 5
    payload = {'Name': f'{IAV.INSPECTED_ADDRESS_VALUE}', 'Limit': f'{limit}'}
    response = requests.get(f'{CM.BASE_URL}{CM.GET_URL_ADDRESS}', params=payload)
    return response