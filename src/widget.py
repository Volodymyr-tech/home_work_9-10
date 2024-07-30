from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(users_input: str) -> str:
    """Функция для масировки номера карты или номера счета клиента"""
    users_input_list = users_input.split()
    name_account_parts = []
    masked_account = ""

    for item in users_input_list:
        if item.isalpha():
            name_account_parts.append(item)
        elif item.isdigit and len(item) == 20:
            masked_account = get_mask_account(item)
        elif item.isdigit and len(item) == 16:
            masked_account = get_mask_card_number(item)

    name_account = " ".join(name_account_parts)
    return f"{name_account} {masked_account}"


def get_date(corrent_data: str) -> str:
    """Функция для возврата даты в корректном формате"""
    date_list = corrent_data.split("T")
    del date_list[1]
    date_string = "".join(date_list)
    date_list = date_string.split("-")

    year = date_list.pop(0)
    month = date_list.pop(1)

    date_list.insert(1, year)
    date_list.insert(0, month)

    return ".".join(date_list)


data = input()
result = get_date(data)
print(result)
