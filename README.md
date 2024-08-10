# Банковские функции
Этот проект предназначен для обработки и маскирования данных, связанных с банковскими картами и счетами клиентов. Он включает функции для фильтрации, сортировки данных по дате, а также для маскирования номеров карт и счетов. Основная цель проекта — обеспечить безопасность и конфиденциальность данных.

## Функционал
- Фильтрация данных: Функция для фильтрации списка данных по заданному состоянию (например, "EXECUTED").
- Сортировка данных: Функция для сортировки списка данных по дате.
- Маскирование номера карты: Функция для маскирования 16-значного номера карты.
- Маскирование номера счета: Функция для маскирования 20-значного номера счета.
- Форматирование даты: Функция для преобразования даты в читаемый формат.
  
## Использование

### Фильтрация и сортировка данных:

- filter_by_state(data: list, state: str = "EXECUTED") -> list
- sort_by_date(sorted_date: list, reverse_date: bool = True) -> list
  
### Маскирование данных:

- get_mask_card_number(card_number: str) -> str
- get_mask_account(account_number: str) -> str
- mask_account_card(users_input: str) -> str
  
### Форматирование даты:

-  get_date(current_date: str) -> str

## Основные функции
- main(): Запрашивает ввод номера банковской карты и номера счета, маскирует их и выводит результат.

### Для работы скрипта необходимо наличие следующих модулей:

- src.masks (содержащий функции get_mask_card_number и get_mask_account)

## Группы зависимостей
### Группа: lint используется для обеспечения качества кода и стиля.

- flake8: ^7.1.0 — инструмент для проверки соответствия кода стандартам PEP 8.
- black: ^24.4.2 — форматтер кода.