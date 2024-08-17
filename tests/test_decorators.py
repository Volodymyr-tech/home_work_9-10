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


def test_raise_error(tmpdir):
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

















def test_error_raise():
    with pytest.raises(ZeroDivisionError, match=r'Ну че ты делишь то\?'):
        result(10,0)


def test_divide():
    assert result(10, 2) == 5

