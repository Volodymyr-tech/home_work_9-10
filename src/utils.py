import json
import os.path
from typing import Any, Dict, List

PATH = r"C:\Users\Владимир\PycharmProjects\homework_9.1\data\operations.json"


def json_reader(path: str) -> List[Dict[str, Any]]:
    """Функция принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях."""
    if not os.path.isfile(path):
        return []

    if os.path.getsize(path) == 0:
        return []

    with open(path, "r", encoding="utf-8") as file:
        output_data = json.load(file)

        if not isinstance(output_data, list):
            return []

        return output_data
