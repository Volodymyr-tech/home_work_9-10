from unittest.mock import patch

import pandas as pd
import pytest

from src.file_readers import pandas_reader_xlsx, reader_csv


@pytest.mark.parametrize(
    "path_csv, output_dict_csv",
    [
        (
            r"C:\Users\Владимир\PycharmProjects\API GitHub\news\students.csv",
            [{"name": "Alice", "age": "20", "avg_grade": "4.7"}],
        )
    ],
)
@patch("csv.DictReader")
def test_csv_reader(mock_dict, path_csv, output_dict_csv):
    # Настройка мок-объекта
    mock_dict.return_value = output_dict_csv

    # Вызов тестируемой функции
    result_value = reader_csv(path_csv)

    # Проверка результата
    assert result_value == output_dict_csv


@pytest.mark.parametrize(
    "path_xlsx, output_dict_xlsx",
    [
        (
            r"C:\Users\Владимир\PycharmProjects\API GitHub\news\sample_employee_data.xlsx",
            [
                {"Name": "Alice", "Department": "HR", "Salary": 70000, "Date Hired": "2020-01-15"},
                {"Name": "Bob", "Department": "Engineering", "Salary": 80000, "Date Hired": "2019-04-22"},
                {"Name": "Charlie", "Department": "Marketing", "Salary": 60000, "Date Hired": "2018-06-18"},
                {"Name": "David", "Department": "Engineering", "Salary": 90000, "Date Hired": "2021-07-30"},
                {"Name": "Eve", "Department": "HR", "Salary": 75000, "Date Hired": "2020-11-12"},
            ],
        )
    ],
)
@patch("pandas.read_excel")
def test_pandas_reader_xlsx(mock_read_excel, path_xlsx, output_dict_xlsx):
    # Создаем DataFrame, который будет возвращен мок-объектом
    df_mock = pd.DataFrame(output_dict_xlsx)

    # Настройка мок-объекта
    mock_read_excel.return_value = df_mock

    # Вызов тестируемой функции
    result = pandas_reader_xlsx(path_xlsx)

    # Проверка результата
    assert result == output_dict_xlsx


@pytest.fixture
def incorrect_path():
    path = r"C:\Users\Владимир\PycharmProjects\API GitHub\news\students.xlsx"
    return path


def test_error_pandas_reader_xlsx(incorrect_path):
    result = pandas_reader_xlsx(incorrect_path)
    assert result == []


def test_error_reader_csv(incorrect_path):
    result = reader_csv(incorrect_path)
    assert result == []
