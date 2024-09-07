import csv
from typing import Any, Dict, List, Union

import pandas as pd


def reader_csv(path: str) -> list[dict[str | Any, str | Any]]:
    """Функция для чтения CSV файла в виде словаря"""
    try:
        with open(path, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file, delimiter=";")
            transactions_data = list(reader)
            return transactions_data

    except FileNotFoundError:
        print("Файл не найден.")
        return []


def pandas_reader_xlsx(path: str) -> Union[Dict[str, Any], List[Any]]:
    """Функция для чтения XLSX файла в виде словаря"""
    try:
        reader = pd.read_excel(path, index_col=0)
        transactions_data = reader.to_dict(orient="records")
        return transactions_data

    except FileNotFoundError:
        print("Файл не найден.")
        return []
