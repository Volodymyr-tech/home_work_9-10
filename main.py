# main.py

from src.masks import get_mask_card_number, get_mask_account


def main():
    user_input = input("Введите номер банковской карты (16 цифр): ")
    try:
        result = get_mask_card_number(user_input)
        print(f"{result}")
    except ValueError as e:
        print(e)

    user_input_2 = input("Введите номер аккаунта (20 цифр): ")
    try:
        result_2 = get_mask_account(user_input_2)
        print(f"{result_2}")
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
