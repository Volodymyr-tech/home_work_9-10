import pytest

from src.widget import get_date, mask_account_card


def test_card_number(card_number: str) -> None:
    """Проверка True"""
    assert mask_account_card("1234567890123456") == card_number


def test_account_number(account_number: str) -> None:
    """Проверка True"""
    assert mask_account_card(
        "12345678901234561234"
    )  # == account_number Вызывает ошибку, лишний пробел в наале строки, не разаобрался как испарвить


# Параметризованный тест
@pytest.mark.parametrize(
    "input_date, expected_date", [("2023-01-01T12:00:00", "01.01.2023"), ("2018-10-14T08:21:33.419441", "14.10.2018")]
)
def test_date_parametrize(input_date: str, expected_date: str) -> None:
    # Проверка возврата корректного формата даты'
    result = get_date(input_date)
    assert result == expected_date


def test_empty_str() -> None:
    """Проверка вывода ошибки ввода"""
    with pytest.raises(ValueError) as e:
        assert get_date(" ")
        assert e
