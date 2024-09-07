# import random
from typing import Any, Dict, Iterator, List


def filter_by_currency(dict_list: List[Dict[str, Any]], currency: str) -> Iterator:
    """Функция для фильтрации транзакций по валюте (учитывает наличие ключей operationAmount и currency_code)"""
    for operation in dict_list:
        # Если есть ключ 'operationAmount', проверяем внутри его
        if (
            "operationAmount" in operation
            and "currency" in operation["operationAmount"]
            and "code" in operation["operationAmount"]["currency"]
        ):
            if operation["operationAmount"]["currency"]["code"] == currency:
                yield operation

        # Если есть ключ 'currency_code', проверяем его
        elif "currency_code" in operation:
            if operation["currency_code"] == currency:
                yield operation


# def filter_by_currency(dict_list: List[Dict[str, Any]], currency: str) -> Iterator:
#     """Функция для вывода валюты транзакции"""
#     for operation in dict_list:
#         if "operationAmount" in operation and operation["operationAmount"]["currency"]["code"] == currency:
#             yield operation
#         elif operation['currency_code'] == 'RUB':
#             yield operation


def transaction_descriptions(dict_transaction: List[Dict[str, Any]]) -> Iterator[str]:
    """Функция для возврата описания транзакции"""
    for info in dict_transaction:
        if "description" in info:
            description = info["description"]
            yield description


def card_number_generator(start: int, stop: int) -> Iterator[str]:
    """Генерация последовательности номеров карт в заданном диапазоне с использованием конкатенации строк"""
    for number in range(start, stop + 1):
        number_str = str(number)

        # Добавляем нули в начале строки до тех пор, пока длина не станет 16 символов
        while len(number_str) < 16:
            number_str = "0" + number_str

        # Форматируем строку
        formatted = number_str[0:4] + " " + number_str[4:8] + " " + number_str[8:12] + " " + number_str[12:]
        yield formatted
