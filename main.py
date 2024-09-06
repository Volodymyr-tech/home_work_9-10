import re

from src.utils import json_reader
from src.processing import filter_by_state, sort_by_date
from src.generators import filter_by_currency, transaction_descriptions
from src.file_readers import reader_csv, pandas_reader_xlsx
from src.serch_string import filter_by_description, count_operations_by_category



file_json = r"C:\Users\Владимир\PycharmProjects\homework_9.1\data\operations.json"
file_csv = r"C:\Users\Владимир\PycharmProjects\homework_9.1\data\transactions.csv"
file_xlsx = r"C:\Users\Владимир\PycharmProjects\homework_9.1\data\transactions_excel.xlsx"
def main() -> None:
    # Получаем список словарей user_input через выбранный способ чтения
    print('Привет! Добро пожаловать в программу работы с банковскими транзакциями.')

    while True:

        user_input = int(input('Выберите необходимый пункт меню:\n1. Получить информацию о транзакциях из JSON-файла\n2. Получить информацию о транзакциях из CSV-файла\n3. Получить информацию о транзакциях из XLSX-файла\n'))

        if user_input in [1,2,3]:
            if user_input == 1:
                print('Для обработки выбран JSON-файл.')
                user_status = input('Введите статус, по которому необходимо выполнить фильтрацию.\nДоступные для фильтровки статусы: EXECUTED, CANCELED, PENDING ').upper()

                if user_status in ['EXECUTED', 'CANCELED', 'PENDING']:
                    json_data = json_reader(file_json)
                    filtered_by_state = filter_by_state(json_data, user_status)
                    break

                else:
                    print(f'Статус операции {user_status} недоступен')
                    user_status = input('Пожалуйста, введите корректный статус (EXECUTED, CANCELED, PENDING): ').upper()

            elif user_input == 2:
                print('Для обработки выбран CSV-файл.')
                user_status = input('Введите статус, по которому необходимо выполнить фильтрацию.\nДоступные для фильтровки статусы: EXECUTED, CANCELED, PENDING ').upper()

                if user_status in ['EXECUTED', 'CANCELED', 'PENDING']:
                    csv_data = reader_csv(file_csv)
                    filtered_by_state = filter_by_state(csv_data, user_status)
                    break

                else:
                    print(f'Статус операции {user_status} недоступен')
                    user_status = input('Пожалуйста, введите корректный статус (EXECUTED, CANCELED, PENDING): ').upper()


            elif user_input == 3:
                print('Для обработки выбран XLSX-файл.')
                user_status = input('Введите статус, по которому необходимо выполнить фильтрацию.\nДоступные для фильтровки статусы: EXECUTED, CANCELED, PENDING ').upper()

                if user_status in ['EXECUTED', 'CANCELED', 'PENDING']:
                    xlsx_data = pandas_reader_xlsx(file_xlsx)
                    filtered_by_state = filter_by_state(xlsx_data, user_status)
                    break

                else:
                    print(f'Статус операции {user_status} недоступен')
                    user_status = input('Пожалуйста, введите корректный статус (EXECUTED, CANCELED, PENDING): ').upper()

        else:
            print('Некорректный выбор. Пожалуйста, выберите 1, 2 или 3.')

    while True:
        user_sort = input('Программа: Отсортировать операции по дате? Да/Нет ').lower()
# Получаем булевое значение и сортируем список
        if user_sort == 'да':
            user_bool = input('Программа: Отсортировать по возрастанию или по убыванию? ')

            false_sort = r'по\s+возрастанию'
            true_sort = r'по\s+убыванию'

            if re.search(true_sort, user_bool):
                sorted_by_date = sort_by_date(filtered_by_state, True)
                break

            elif re.search(false_sort, user_bool):
                sorted_by_date = sort_by_date(filtered_by_state, False)
                break

        elif user_sort == 'нет':
            sorted_by_date = filtered_by_state
            break


        else:
            print(f'Ващ ввод {user_sort} не поддерживается. Введите "Да/Нет" ')


    while True:
        user_currency = input('Выводить только рублевые тразакции? Да/Нет ').lower()

        if user_currency in ['да', 'нет']:
            if user_currency == 'да':
                filtered_by_currency = filter_by_currency(sorted_by_date, 'RUB')
                break
            elif user_currency == 'нет':
                filtered_by_currency = sorted_by_date
                break
        else:
            user_currency = input(f'Ващ ввод {user_currency} не поддерживается. Введите "Да/Нет" ').lower()


    while True:
        filter_by_word = input('Отфильтровать список транзакций по определенному слову в описании? Да/Нет ')
        if filter_by_word in ['да', 'нет']:
            if filter_by_word == 'да':
                search_word = input('Введи ключевое слово для фильтрации')
                sorted_by_word = filter_by_description(filtered_by_currency, search_word)
                break
            elif filter_by_word == 'нет':
                sorted_by_word = filtered_by_currency
                break
            else:
                search_word = input(f'Ваш ввод {filter_by_word} не поддерживается. Введите "Да/Нет" ').lower()

    print('Распечатываю итоговый список транзакций...')

    print(type(filter_by_word))





        #
        #
        #
        #     if re.search(true_sort, user_bool, re.IGNORECASE):
        #         sorted_by_date = sort_by_date(filtered_by_state, True)
        #
        #     elif re.search(false_sort, user_bool):
        #         sorted_by_date = sort_by_date(filtered_by_state, False)
        #
        #     else:
        #         print('Некорректный ввод для сортировки. Выход.')
        #
        #

        #         return
        #
        # word_filter = input('Программа: Отфильтровать список транзакций по определенному слову в описании? Да/Нет ').lower()
        #
        # if word_filter == 'да':
        #     description_data = list(transaction_descriptions(filtered_currency))
        #     print(f"Транзакции после фильтрации по описанию: {description_data}")
        #     if not description_data:
        #         print("Нет транзакций с таким описанием.")
        #         return
        #
        #     print('Программа: Распечатываю итоговый список транзакций...')
        #     for description in description_data:
        #         print(description)
        # else:
        #     print('Программа: Распечатываю список транзакций без фильтрации по описанию...')
        #     for transaction in filtered_currency:
        #         print(transaction)
        #
        # # else:
        # #     print('Сортировка не выполнена. Выход.')
        # #
        # # elif user_input == 2:
        # #     print('Для обработки выбран CSV-файл')
        # #     # Действия для работы с CSV
        # #
        # # elif user_input == 3:
        # #     print('Для обработки выбран XLSX-файл')
        # #     # Действия для работы с XLSX


if __name__ == "__main__":
    main()

