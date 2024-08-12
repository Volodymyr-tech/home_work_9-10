from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(users_input: str) -> str:
    """Функция для масировки номера карты или номера счета клиента"""
    users_input_list = users_input.split()
    name_account_parts = []
    masked_account = ""

    for item in users_input_list:
        if item.isalpha():
            name_account_parts.append(item)
        elif item.isdigit() and len(item) == 20:
            masked_account = get_mask_account(item)
        elif item.isdigit() and len(item) == 16:
            masked_account = get_mask_card_number(item)

        name_account = " ".join(name_account_parts)

    return f"{name_account} {masked_account}"


def get_date(current_date: str) -> str:
    """Функция для возврата корректного формата даты"""
    date_part = current_date.split("T")[0]

    year, month, day = date_part.split("-")

    formatted_date = f"{day}.{month}.{year}"

    return formatted_date
