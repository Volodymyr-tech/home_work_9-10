import pytest


@pytest.fixture
def card_number() -> str:
    return " 1234 56** **** 3456"


@pytest.fixture
def account_number() -> str:
    return "**1234"


@pytest.fixture
def error_raise() -> None:
    return ValueError


@pytest.fixture
def space_input() -> None:
    return ValueError


@pytest.fixture
def sample_data() -> list:
    return [
        {"id": 1, "state": "EXECUTED", "date": "2023-01-01T12:00:00"},
        {"id": 2, "state": "CANCELED", "date": "2023-01-02T12:00:00"},
        {"id": 3, "state": "EXECUTED", "date": "2023-01-03T12:00:00"},
        {"id": 4, "state": "PENDING", "date": "2023-01-04T12:00:00"},
    ]


@pytest.fixture
def sample_time() -> list:
    return ["2023-01-01T12:00:00", "2018-10-14T08:21:33.419441"]


@pytest.fixture
def expected_dates() -> list:
    return ["01.01.2023", "14.10.2018"]


@pytest.fixture
def data_to_process() -> list:
    return [
        {"id": 1, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 4, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 3, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 2, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]
