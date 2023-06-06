# Напишите декоратор func_log, который может принимать аргумент file_log (Путь до файла), по умолчнию равен 'log.txt'
# Декоратор должен дозаписывать в файл имя вызываемой функции (можно получить по атрибуту __name__), дату и время вызова
# по формату:
# имя_функции вызвана %d.%m %H:%M:%S
# Для вывода времени нужно использовать модуль datetime и метод .strftime()
# https://pythonworld.ru/moduli/modul-datetime.html
# https://docs.python.org/3/library/datetime.html
#
# Например
# @func_log()
# def func1():
#     time.sleep(3)
#
# @func_log(file_log='func2.txt')
# def func2():
#     time.sleep(5)
#
# func1()
# func2()
# func1()
#
# Получим:
# в log.txt текст:
# func1 вызвана 30.05 14:12:42
# func1 вызвана 30.05 14:12:50
# в func2.txt текст:
# func2 вызвана 30.05 14:12:47

# Со звёздочкой. ДЕЛАТЬ НЕ ОБЯЗАТЕЛЬНО.
# help(func1) должен выводит одинаковый текст, когда есть декоратор на функции func1 и когда его нет
# Реализовать без подключения новых модулей и сторонних библиотек.


import datetime


def func_log(file_log='log.txt'):
    """Декоратор который в текстовый файл записывает время вызова функции
    :param file_log: аргумент с путем/названием файла в который записываем логи вызова функции"""
    def path_log(func):
        def wrapper(*args, **kwargs):
            date_today = datetime.datetime.today().strftime('%d.%m %H:%M:%S')
            name_func = func.__name__
            with open(file_log, 'a', encoding='utf-8') as logs:
                logs.write(f'{name_func} {date_today} \n')
            return func()
        wrapper.__name__ = func.__name__
        wrapper.__doc__ = func.__doc__
        return wrapper
    return path_log


@func_log()
def func1():
    """Функция ничего не делает, нужна для проверки декоратора с дефолтным значением"""
    pass


@func_log(file_log='test_file/text_log1.txt')
def func2():
    """Функция ничего не делает, нужна для проверки декоратора с кастомным значением"""
    pass


help(func1)


def func1():
    """Функция ничего не делает, нужна для проверки декоратора с дефолтным значением"""
    pass


print('_______')
help(func1)

