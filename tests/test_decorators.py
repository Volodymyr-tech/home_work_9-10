import pytest
from src.decorators import log


def test_log_decorator(tmpdir):
    log_info = tmpdir.join('test_log.txt')

    @log(log_info)
    def greet():
        return 'Hello'

    res = greet()

    assert res == 'Hello'

    with open(log_info, 'r', encoding='utf-8') as file:
        content = file.read()
        assert 'Запуск функции: greet ok' in content
        assert 'Функция greet выполнена.' in content


def test_log_raise_error(tmpdir):
    error_info = tmpdir.join('test_eror_log.txt')

    @log(error_info)
    def result(x, y):
        if y == 0:
            raise ZeroDivisionError('Ну че ты делишь то?')
        else:
            nums = x / y
            return nums

    with pytest.raises(ZeroDivisionError):
        result(10,0)

    with open(error_info, 'r', encoding='utf-8') as file:
        content = file.read()

        assert 'result error: ZeroDivisionError. Inputs: (10, 0), {}\n' in content


def test_log_capsys(capsys):
    @log()
    def greet():
        return 'Hello'

    greet()
    captured = capsys.readouterr()
    expected_output = (
        'Запуск функции: greet ok\n'
        'Функция greet выполнена.\n'  # Добавляем \n в конце
        '\n'  # Дополнительный символ новой строки
    )
    assert captured.out == expected_output

def test_log_capsys_error(capsys):
    @log()
    def result(x, y):
        if y == 0:
            raise ZeroDivisionError('Ну че ты делишь то?')
        else:
            nums = x / y
            return nums

    with pytest.raises(ZeroDivisionError):
        result(10, 0)

    captured = capsys.readouterr()
    expected_output = ('result error: ZeroDivisionError.Inputs: (10, 0), {}\n\n')
    assert captured.out == expected_output


