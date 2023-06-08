# Напишите 5 тестов на функцию all_division. Обязательно должен быть тест деления на ноль.
# Промаркируйте часть тестов. Например, smoke.
# В консоли с помощью pytest сделайте вызов:
# 1) Всех тестов
# 2) Только с маркером smoke
# 3) По маске. Выберите такую маску, чтобы под неё подпадали не все тесты, но больше одного
# Пришлите на проверку файл с тестами и скрины с вызовами и их результаты

import pytest


def all_division(*arg1):

    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


def test_1():
    """Тест №1 """
    assert all_division(3, 6) == 0.5


@pytest.mark.aссeptance
def test_2():
    """Тест №2"""
    assert all_division(3, 4, 6) == 0.125


@pytest.mark.smoke
def test_3_my_tree():
    """Тест №3"""
    assert all_division(3, 1) == 3


def test_4_my():
    """Тест №4"""
    assert all_division(1, 1) == 1


def test_5_zero_division():
    """Тест №5 с делением на ноль"""
    with pytest.raises(ZeroDivisionError):
        all_division(1, 0, 0)
