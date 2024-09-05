import pytest
from src.serch_string import filter_by_description, count_operations_by_category


@pytest.mark.parametrize('data, output, pattern', [( [
    {"id": 1, "description": "Перевод на счет", "amount": 100},
    {"id": 2, "description": "Оплата услуг", "amount": 200},
    {"id": 3, "description": "Перевод организации", "amount": 300},
    {"id": 4, "description": "Покупка товара", "amount": 400}],
    [{'id': 1, 'description': 'Перевод на счет', 'amount': 100}, {'id': 3, 'description': 'Перевод организации', 'amount': 300}], 'Перевод')])

def test_filter_by_description(data, output, pattern):
    """Функция для тестирования возврата списка словарей, у которых в описании есть заданная строка."""
    result = filter_by_description(data, pattern)
    assert result == output


@pytest.mark.parametrize('data_category, output_data, category',[([
    {"id": 1, "description": "Перевод на счет", "amount": 100},
    {"id": 2, "description": "Покупка услуг", "amount": 200},
    {"id": 3, "description": "Перевод организации", "amount": 300},
    {"id": 4, "description": "Покупка товара", "amount": 400},
    {"id": 5, "description": "Оплата налогов", "amount": 500},
    {"id": 6, "description": "Покупка физ. лицу", "amount": 600}
], {'Перевод': 2, 'Покупка': 3, 'Оплата': 1}, ["Перевод", "Оплата", "Покупка"])])

def test_count_operations_by_category(data_category, output_data, category):
    """Функция для тестирования возврата словаря, в котором ключи — это названия категорий, а значения — это количество операций в каждой категории."""
    result = count_operations_by_category(data_category, category)
    assert result == output_data