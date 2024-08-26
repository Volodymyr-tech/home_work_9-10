import pytest
import requests
from unittest.mock import patch, Mock
from src.external_api import convert


@pytest.mark.parametrize(
    "data, output",
    [
        ([
  {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
  }], 'Сумма в рублях: 31957.58'),  # Обратная сортировка
    ],
)
def test_convert_transaction_rub(data, output):
    result = next(convert(data))
    assert result == output


@pytest.mark.parametrize(
    "data_json, expected_result",
    [
        # Пример с валютой не в рублях и курсом 100
        ([{
            "operationAmount": {
                "amount": "100.0",
                "currency": {
                    "code": "USD"
                }
            }
        }], 'Сумма в рублях: 10000.0')  # Результат будет 10000 RUB при курсе 100
    ]
)


@patch('requests.request')
def test_convert(mock_request, data_json, expected_result):
    # Настройка замоканного ответа
    mock_response = Mock() #Создание мока
    mock_response.status_code = 200 # задаем статус код моку
    mock_response.json.return_value = {
        "result": 10000.0  # Имитируем ответ json
    }

    mock_response.text = "Mocked response text" #тест для примера записси в лог
    mock_request.return_value = mock_response

    # Проверка генератора
    result_value = next(convert(data_json))

    # Сравнение значений
    assert result_value == expected_result
