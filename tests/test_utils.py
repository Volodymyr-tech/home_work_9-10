import pytest

from src.utils import json_reader


@pytest.fixture
def empty_list():
    return []


@pytest.fixture
def incorect_path():
    path = r"C:\Users\Владимир\PycharmProjects\homework_9.1\data"
    return path


@pytest.fixture
def dictionary():
    data = '{"name": "John Smith", "age": 30, "city": "New York"}'
    return data


def test_incorect_path_json_reader(incorect_path, empty_list):
    assert json_reader(incorect_path) == empty_list


def test_getsize_json_reader(tmpdir, empty_list):
    file = tmpdir.join("test.json")
    file.write("")

    result = json_reader(str(file))

    # Проверяем, что результатом выполнения функции будет пустой список
    assert result == empty_list


def test_not_isinstance_json_reader(tmpdir, empty_list, dictionary):
    file = tmpdir.join("test.json")
    with open(file, "w", encoding="utf-8") as file:
        file.write(dictionary)

    result = json_reader(str(file))

    # Проверяем, что результатом выполнения функции будет пустой список
    assert result == empty_list
