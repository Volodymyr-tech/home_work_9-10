import pandas as pd
import csv

def reader_csv(path: str) -> dict:
    '''Функция для чтения CSV файла в виде словаря'''
    try:
        with open(path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            transactions_data = list(reader)
            return transactions_data

    except FileNotFoundError:
        print((f"Файл не найден."))
        return []


def pandas_reader_xlsx(path: str) -> dict:
    try:
        reader = pd.read_excel(path, index_col=0)
        transactions_data = reader.to_dict(orient='records')
        return transactions_data

    except FileNotFoundError:
        print((f"Файл не найден."))
        return []
