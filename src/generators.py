import random
from typing import Any, Dict, Iterator, List


def filter_by_currency(dict_list: List[Dict[str, Any]], corrency: str) -> Iterator:
    """Функция для вывода валюты транзакции"""
    for operation in dict_list:
        if "operationAmount" and corrency in operation:
 #           input_currency = operation["operationAmount"]["currency"]["name"]
            yield operation
        else:
            raise KeyError

        break


def transaction_descriptions(dict_transaction: List[Dict[str, Any]]) -> Iterator[str]:
    """Функция для возврата описания транзакции"""
    for info in dict_transaction:
        if "description" in info:
            description = info["description"]
            yield description
        else:
            raise KeyError


def card_number_generator(start: int, stop: int) -> Iterator:
    """Функция генерации случайных номеров банковских карт"""
    while True:
        numbers = random.randint(start, stop)
        number_str = str(numbers)

        while len(number_str) < 16:
            number_str = "0" + number_str
            formated = f"{number_str[0:4]} {number_str[4:8]} {number_str[8:12]} {number_str[12:]}"
            yield formated
