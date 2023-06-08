# Напишите генератор generate_random_name(), используя модуль random,
# который генерирует два слова из латинских букв от 1 до 15 символов, разделенных пробелами
# Например при исполнении следующего кода:
# gen = generate_random_name()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
#
# Выводится:
# tahxmckzexgdyt ocapwy
# dxqebbukr jg
# aym jpvezfqexlv
# iuy qnikkgxvxfxtxv

import random


# Здесь пишем код
import string


def generate_random_name():
    """
    Генератор который возвращается два слова из латинских букв длинной от 1 до 15 символов
    Правда не будет работать если максимальное количество символов в слове сделать больше чем длинна латинского алфавита
    =)
    """
    def generate_str():
        return ''.join(random.sample(string.ascii_lowercase, random.randint(1, 15)))
    while True:
        yield f'{generate_str()} {generate_str()}'


gen = generate_random_name()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
