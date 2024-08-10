import pytest

from src.masks import get_mask_account, get_mask_card_number


def test_number_true() -> None:
    """Проверка True"""
    assert get_mask_card_number("1656565647895465") == "1656 56** **** 5465"


def test_space_in_number() -> None:
    """Проверка вывода ошибки ввода"""
    with pytest.raises(ValueError, match="Ошибка! Номер карты должен состоять из 16 цифр без пробелов."):
        get_mask_card_number("1232654564 654654")


def test_space_input_number() -> None:
    """Проверка вывода ошибки ввода"""
    with pytest.raises(ValueError, match="Ошибка! Номер карты должен состоять из 16 цифр без пробелов."):
        get_mask_card_number(" ")


def test_len_number() -> None:
    """Проверка вывода ошибки ввода"""
    with pytest.raises(ValueError, match="Ошибка! Номер карты должен состоять из 16 цифр без пробелов."):
        get_mask_card_number("12345678987456321")


def test_alpha_in_number() -> None:
    """Проверка вывода ошибки ввода"""
    with pytest.raises(ValueError, match="Ошибка! Номер карты должен состоять из 16 цифр без пробелов."):
        get_mask_card_number("addffd1236545698")


def test_account_true() -> None:
    """Проверка True"""
    assert get_mask_account("12123215232123654789") == "**4789"


def test_alpha_in_account() -> None:
    """Проверка вывода ошибки ввода"""
    with pytest.raises(ValueError, match="Ошибка! Номер карты должен состоять из 20 цифр без пробелов."):
        get_mask_account("1232565454556548465a")


def test_len_account() -> None:
    """Проверка вывода ошибки ввода"""
    with pytest.raises(ValueError, match="Ошибка! Номер карты должен состоять из 20 цифр без пробелов."):
        get_mask_account("1236545698")


def test_space_in_account() -> None:
    """Проверка вывода ошибки ввода"""
    with pytest.raises(ValueError, match="Ошибка! Номер карты должен состоять из 20 цифр без пробелов."):
        get_mask_account("123456789 1236547895")


def test_space_input_account() -> None:
    """Проверка вывода ошибки ввода"""
    with pytest.raises(ValueError, match="Ошибка! Номер карты должен состоять из 20 цифр без пробелов."):
        get_mask_account(" ")
