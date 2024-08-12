import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.mark.parametrize(
    "state, expected_ids",
    [
        ("EXECUTED", [1, 3]),
        ("CANCELED", [2]),
        ("PENDING", [4]),
        ("NOT_EXIST", []),  # Проверка случая, когда нет совпадений
    ],
)
def test_filter_by_state(sample_data: list, state: str, expected_ids: list) -> None:
    result = filter_by_state(sample_data, state)
    result_ids = []

    for item in result:
        result_ids.append(item["id"])
    assert result_ids == expected_ids


@pytest.mark.parametrize(
    "reverse, expected_order",
    [
        (True, [1, 2, 3, 4]),  # Обратная сортировка
        (False, [4, 3, 2, 1]),  # Прямая сортировка
    ],
)
def test_sort_by_date(data_to_process: list, reverse: bool, expected_order: list) -> None:
    result = sort_by_date(data_to_process, reverse)

    result_ids = [item["id"] for item in result]

    assert result_ids == expected_order
