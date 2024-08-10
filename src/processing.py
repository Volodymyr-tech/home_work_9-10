def filter_by_state(data: list, state: str = "EXECUTED") -> list:
    """Функция возвращающая список словарей по ключу State"""
    new_data = []
    for status in data:
        if status.get("state") == state:
            new_data.append(status)
    return new_data


def sort_by_date(sorted_date: list, reverse_date: bool = True) -> list:
    """Функция для сортировки списка словарей по дате"""
    sorted_date_list = sorted(sorted_date, key=lambda x: x["date"], reverse=reverse_date)
    return sorted_date_list


if __name__ == "__main__":
    """Проверка работы функциии"""
    data_to_process = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]
    filtered_result = filter_by_state(data_to_process)
    result_sorted = sort_by_date(data_to_process)
    print(filtered_result, "\n", result_sorted)
