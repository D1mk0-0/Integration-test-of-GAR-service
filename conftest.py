import pytest
import requests

@pytest.fixture
def api_client():
    return requests.Session()