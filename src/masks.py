import logging

path_to_log = r'C:\Users\Владимир\PycharmProjects\homework_9.1\logs\masks.log'

logging.basicConfig(filename= path_to_log, filemode='w', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG, encoding='utf-8')
card_logger = logging.getLogger('get_mask_card_number')
mask_logger = logging.getLogger('get_mask_account')

def get_mask_card_number(card_number: str) -> str:
    """Функция возвращает замаскированный номер карты"""
    card_logger.info('Проверяю, номер карты')
    if card_number.isdigit() and len(card_number) == 16:
        card_logger.info('Все гуд, отдаю маску для номера карты')
        masked_number = f"{card_number[0:4]} {card_number[4:6]}** **** {card_number[-4:]}"
        return masked_number
    else:
        card_logger.error('Воуууу, ошибка!')
        raise ValueError("Ошибка! Номер карты должен состоять из 16 цифр без пробелов.")


def get_mask_account(account_number: str) -> str:
    """Функция возвращает замаскированный номер аккаунта"""
    mask_logger.info('Проверяю, номер аккаунта')
    if account_number.isdigit() and len(account_number) == 20:
        mask_logger.info('Все гуд, отдаю маску для номера аккаунта')
        masked_account = f"**{account_number[-4:]}"
        return masked_account
    else:
        mask_logger.error('Воуууу, ошибка!')
        raise ValueError("Ошибка! Номер карты должен состоять из 20 цифр без пробелов.")
