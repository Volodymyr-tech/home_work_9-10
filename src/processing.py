def filter_by_state(data: list, state: str = None) -> list:
    """Функция возвращающая список словарей по ключу State"""
    new_data = []
    for status in data:
        if status.get("state") == state:
            new_data.append(status)
    return new_data


def sort_by_date(sorted_date: list, reverse_date: bool = False) -> list:
    """Функция для сортировки списка словарей по дате"""
    sorted_date_list = sorted(sorted_date, key=lambda x: x["date"], reverse=reverse_date)
    return sorted_date_list



