from src.file_readers import pandas_reader_xlsx, reader_csv
from src.generators import filter_by_currency
from src.processing import filter_by_state, sort_by_date
from src.serch_string import filter_by_description
from src.utils import json_reader
from src.widget import get_date, mask_account_card

file_json = r"C:\Users\Владимир\PycharmProjects\homework_9.1\data\operations.json"
file_csv = r"C:\Users\Владимир\PycharmProjects\homework_9.1\data\transactions.csv"
file_xlsx = r"C:\Users\Владимир\PycharmProjects\homework_9.1\data\transactions_excel.xlsx"


def main() -> None:
    # Получаем список словарей user_input через выбранный способ чтения
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")

    while True:

        user_input = int(
            input(
                "Выберите необходимый пункт меню:\n1. Получить информацию о транзакциях из JSON-файла\n2."
                " Получить информацию о транзакциях из CSV-файла\n3. Получить информацию о транзакциях из XLSX-файла\n"
            )
        )

        if user_input in [1, 2, 3]:
            if user_input == 1:
                print("Для обработки выбран JSON-файл.")
                user_status = input(
                    "Введите статус, по которому необходимо выполнить фильтрацию.\n"
                    "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING "
                ).upper()

                if user_status in ["EXECUTED", "CANCELED", "PENDING"]:
                    json_data = json_reader(file_json)
                    filtered_by_state = filter_by_state(json_data, user_status)
                    print(filtered_by_state)
                    break

                else:
                    print(f"Статус операции {user_status} недоступен")

            elif user_input == 2:
                print("Для обработки выбран CSV-файл.")
                user_status = input(
                    "Введите статус, по которому необходимо выполнить фильтрацию.\n"
                    "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING "
                ).upper()

                if user_status in ["EXECUTED", "CANCELED", "PENDING"]:
                    csv_data = reader_csv(file_csv)
                    print(csv_data)
                    filtered_by_state = filter_by_state(csv_data, user_status)
                    print(filtered_by_state)
                    break

                else:
                    print(f"Статус операции {user_status} недоступен")

            elif user_input == 3:
                print("Для обработки выбран XLSX-файл.")
                user_status = input(
                    "Введите статус, по которому необходимо выполнить фильтрацию.\n"
                    "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING "
                ).upper()

                if user_status in ["EXECUTED", "CANCELED", "PENDING"]:
                    xlsx_data = pandas_reader_xlsx(file_xlsx)
                    filtered_by_state = filter_by_state(xlsx_data, user_status)
                    print(filtered_by_state)
                    break

                else:
                    print(f"Статус операции {user_status} недоступен")

        else:
            print("Некорректный выбор. Пожалуйста, выберите 1, 2 или 3.")

    while True:
        user_sort = input("Программа: Отсортировать операции по дате? Да/Нет ").lower()
        # Получаем булевое значение и сортируем список
        if user_sort == "да":
            user_bool = input("Программа: Отсортировать по возрастанию или по убыванию? ")

            if "убыванию" in user_bool:
                sorted_by_date = sort_by_date(filtered_by_state, True)
                print(sorted_by_date)
                break
            elif "возрастанию" in user_bool:
                sorted_by_date = sort_by_date(filtered_by_state, False)
                print(sorted_by_date)
                break

        elif user_sort == "нет":
            sorted_by_date = filtered_by_state
            print(sorted_by_date)
            break

        else:
            print(f'Ващ ввод {user_sort} не поддерживается. Введите "Да/Нет" ')

    while True:
        user_currency = input("Выводить только рублевые тразакции? Да/Нет ").lower()

        if user_currency in ["да", "нет"]:
            if user_currency == "да":
                filtered_by_currency = list(filter_by_currency(sorted_by_date, "RUB"))
                print(filtered_by_currency)
                break
            elif user_currency == "нет":
                filtered_by_currency = sorted_by_date
                print(filtered_by_currency)
                break
        else:
            user_currency = input(f'Ващ ввод {user_currency} не поддерживается. Введите "Да/Нет" ').lower()

    while True:
        filter_by_word = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет ")
        if filter_by_word in ["да", "нет"]:
            if filter_by_word == "да":
                search_word = input("Введи ключевое слово для фильтрации")
                sorted_by_word = filter_by_description(filtered_by_currency, search_word)
                break
            elif filter_by_word == "нет":
                sorted_by_word = filtered_by_currency
                break
        else:
            filter_by_word = input(f'Ваш ввод {filter_by_word} не поддерживается. Введите "Да/Нет" ').lower()

    print("Распечатываю итоговый список транзакций...")

    print(sorted_by_word)

    if len(sorted_by_word) == 0:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    else:
        # print(f"Всего банковских операций в выборке: {count_operations_by_category(sorted_by_word, [search_word])}")
        print(f"Всего банковских операций в выборке: {len(sorted_by_word)}")
        print(" ")

        for i in sorted_by_word:
            print(f"{get_date(i['date'])} {str(i['description'])}")
            if i["description"] == "Открытие вклада":
                print(f"Счет: {mask_account_card(i['to'])}")
                print(f"Сумма: {i['operationAmount'].get('amount')}\n")
            elif i["description"] == "Перевод организации":
                print(f"{mask_account_card(str(i['from']))} -> {mask_account_card(str(i['to']))}")
                print(f"Сумма: {i['operationAmount'].get('amount')}\n")
            elif i["description"] == "Перевод с карты на карту":
                print(f"{mask_account_card(str(i['from']))} -> {mask_account_card(str(i['to']))}")
                print(f"Сумма: {i['operationAmount'].get('amount')}\n")
            elif i["description"] == "Перевод со счета на счет":
                print(f"{mask_account_card(str(i['from']))} -> {mask_account_card(str(i['to']))}")
                print(f"Сумма: {i['operationAmount'].get('amount')}\n")


if __name__ == "__main__":
    main()
