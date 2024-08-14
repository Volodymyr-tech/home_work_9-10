import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


@pytest.fixture
def transaction():
    """Список словарей с вложенными словарями"""
    return [
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
    ]


@pytest.fixture
def currency():
    """Валюта"""
    return "USD"


@pytest.fixture
def sorted_dict():
    """Словарь отсортирован по валюте USD"""
    return [
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        }
    ]


@pytest.fixture
def transaction_descriptions_fixture(transaction):
    """Функция для возврата описания транзакции"""
    descriptions = [trans["description"] for trans in transaction]
    return descriptions


@pytest.mark.parametrize("start, end, expected", [(1, 1, ["0000 0000 0000 0001"])])
def test_generated_number(start, end, expected):
    """Функция для тестирования генерации номера карты"""
    result = list(card_number_generator(start, end))
    assert result == expected


def test_filter_by_currency(transaction, currency, sorted_dict):
    """Функция для тестирования фильтрации по валюте"""
    result = list(filter_by_currency(transaction, currency))
    assert result == sorted_dict


def test_transaction_descriptions(transaction, transaction_descriptions_fixture):
    """Функция для тестирования вывода описания транзакции"""
    result = list(transaction_descriptions(transaction))
    assert result == transaction_descriptions_fixture
