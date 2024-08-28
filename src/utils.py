import json
import logging
import os.path
from typing import Any, Dict, List

logger = logging.getLogger("utils")
file_handler = logging.FileHandler(r"C:\Users\Владимир\PycharmProjects\homework_9.1\logs\utils.log", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)

logger.setLevel(logging.DEBUG)  # setting up logger level to react


PATH = r"C:\Users\Владимир\PycharmProjects\homework_9.1\data\operations.json"


def json_reader(path: str) -> List[Dict[str, Any]]:
    """Функция принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях."""
    logger.info("Проверяю, что файл существует")
    if not os.path.isfile(path):
        return []

    logger.info("Проверяю, файл не пустой")
    if os.path.getsize(path) == 0:
        return []

    with open(path, "r", encoding="utf-8") as file:
        output_data = json.load(file)
        logger.info("Читаем JSON файл")

        logger.info("Проверяю, что файл содержит список")
        if not isinstance(output_data, list):
            return []

        logger.info("Программа завершена")
        return output_data
