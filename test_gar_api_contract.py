import requests
import pytest

#from spellchecker import SpellChecker <-- Для проверки орфографии (Пока неактивно)

BASE_URL = 'http://gar.gblinov.ru:18181'
GET_URL = '/v1/Addresses'

address_base_set = [
    ['город Москва, 2-й Тушинский проезд, дом 8'],
    ['г Москва, ул Ботаническая М., д. 16, кв. 13'],
    ['г Москва, ул М. Ботаническая, д. 16, кв. 13'],
    ['г Москва, ул Ботаническая Малая, д. 16, кв. 13'],
    ['г Москва, ул Малая Ботаническая, д. 16, кв. 13'],
    ['г Москва, ул Ботаническая, д. 16, кв. 13'],
    ['город Москва, улица Ефремова, дом 19, строение 6'],
    ['город Москва, Домодедовская улица, дом 34, корпус 1'],
    ['город Москва, Авиационная улица, сооружение 79/1, строение 3'],
    ['город Москва, Днепропетровская улица, дом 16, корпус 2, строение 2'],
    ['город Москва, поселение "Мосрентген", квартал № 8, дом 293, строение 1'],
    ['город Москва, поселение Новофедоровское, деревня Кузнецово, 3-й Заречный переулок, дом 3, строение 2'],
    ['г. Москва, ш. Можайское, 45,4,3'],
    ['Москва, ул. Сухонская д 11, кв 2'],
    ['город М'],
    ['город Москва, улица Римского'],
    ['город Москва, Старая Басманная'],
    ['город Москва, Новая Басманная'],
]

def count_matching_items(list1, list2):
    return len(set(list1).intersection(list2))

@pytest.mark.parametrize(
    argnames=['address'],
    argvalues=address_base_set
)
def test_should_be_api_address_contract(address):
    if address == 'город М':
        pytest.xfail(f'Слишком уж некорректный адрес: {address}')
        return
    payload = {'Name': f'{address}', 'Limit': '10'}
    response = requests.get(f'{BASE_URL}{GET_URL}', params=payload)
    assert response.status_code == 200, \
        f'\nСтатус ответа не в порядке :{response.status_code}'
    response_json = response.json()
    response_address = response_json[0]['name']['default']
    list_address = address.split()
    list_response_address = response_address.split()
    hint_quality_index = count_matching_items(list_address, list_response_address)
    print(f'\nИндекс качества подсказки: {hint_quality_index}')
    assert hint_quality_index >= 2, \
        f'Для запроса: "{address}" - слишком низкий индекс качества подсказки = {hint_quality_index}. ' \
        f'Была возвращена подсказка: {response_address}'

if __name__ == "__main__":
    pytest.main([__file__])