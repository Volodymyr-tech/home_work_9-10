def get_mask_card_number(card_number: str) -> str:
    """Функция возвращает замаскированный номер карты"""
    if card_number.isdigit() and len(card_number) == 16:
        masked_number = f"{card_number[0:4]} {card_number[4:6]}** **** {card_number[-4:]}"
        return masked_number
    else:
        raise ValueError("Ошибка! Номер карты должен состоять из 16 цифр без пробелов.")


def get_mask_account(account_number: str) -> str:
    """Функция возвращает замаскированный номер аккаунта"""
    if account_number.isdigit() and len(account_number) == 20:
        masked_account = f"{'*' * 16}{account_number[-4:]}"
        return masked_account
    else:
        raise ValueError("Ошибка! Номер карты должен состоять из 20 цифр без пробелов.")
