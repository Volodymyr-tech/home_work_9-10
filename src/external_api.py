import os

import requests
from dotenv import load_dotenv

from src.utils import json_reader

load_dotenv()
PATH = r"C:\Users\Владимир\PycharmProjects\homework_9.1\data\operations.json"
path_log = r"C:\Users\Владимир\PycharmProjects\homework_9.1\data\api_response.log"
api_key = os.getenv("API_KEY")


def convert(transactions):
    """Функция конвертации любой валюты в рубли"""
    for transaction in transactions:
        if "operationAmount" in transaction and (transaction["operationAmount"]["currency"]["code"] == "RUB"):
            yield f'Сумма в рублях: {float(transaction["operationAmount"]["amount"])}'

        elif "operationAmount" in transaction and (transaction["operationAmount"]["currency"]["code"] != "RUB"):
            headers = {"apikey": api_key}

            payload = {
                "amount": transaction["operationAmount"]["amount"],
                "from": transaction["operationAmount"]["currency"]["code"],
                "to": "RUB",
            }

            url = f'https://api.apilayer.com/exchangerates_data/convert?to={payload["to"]}&from={payload["from"]}&amount={payload["amount"]}'

            try:

                response = requests.request("GET", url, headers=headers, params=payload, timeout=60)
                status_code = response.status_code

                with open(path_log, "a", encoding="utf-8") as logfile:
                    logfile.write(response.text + "\n")

                if status_code == 200:
                    result = response.json()

                    yield f'Сумма в рублях: {float(result["result"])}'

            except requests.exceptions.ConnectionError:
                print("Connection Error. Please check your network connection.")


if __name__ == "__main__":
    transactions = json_reader(PATH)

    # Создаём генератор
    result_generator = convert(transactions)

    # Получаем первую транзакцию
    print(next(result_generator))
