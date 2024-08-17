import logging

logging.basicConfig(level=logging.INFO)


def log(filename=None):
    def decorator(function):
        def wrapper(*args, **kwargs):
            log_message = (
                f"Запуск функции: {function.__name__} ok\n"
                f"Функция {function.__name__} выполнена.\n"
            )
            try:
                result = function(*args, **kwargs)

                if filename:
                    with open(filename, 'a', encoding='utf-8') as file:
                        file.write(log_message + "-" * 40 + "\n")
                else:
                    print(log_message)

                return result  # Добавляем возврат результата выполнения функции

            except Exception as e:
                error_message = f"{function.__name__} error: {e.__class__.__name__}. Inputs: {args}, {kwargs}\n"

                if filename:
                    with open(filename, "a", encoding='utf-8') as file:
                        file.write(error_message)
                else:
                    print(error_message)

                raise

        return wrapper

    return decorator