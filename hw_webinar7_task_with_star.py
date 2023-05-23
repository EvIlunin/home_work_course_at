# Напишите класс RomanNums
# Экземпляр класса создается из строки - Римского числа.
# Реализуйте методы класса:
# 1. from_roman, который переводит римскую запись числа в арабскую
# 2. is_palindrome, метод определяет, является ли арабское число палиндромом (True - является, иначе False)
# т.е. имеет ли одинаковое значение число при чтении слева направо и справа налево
# Например (Ввод --> Вывод) :
# RomanNums('MMMCCLXIII').from_roman() --> 3263
# RomanNums('CMXCIX').is_palindrome() --> True

class RomanNums:
    """Класс для работы с римскими цифрами"""

    roman_arab_dict = {
        'M': 1000,
        'CM': 900,
        'D': 500,
        'CD': 400,
        'C': 100,
        'XC': 90,
        'L': 50,
        'XL': 40,
        'X': 10,
        'IX': 9,
        'V': 5,
        'IV': 4,
        'I': 1,
    }

    def __init__(self, roman_num):
        """"""

        self.roman_num = roman_num

    def from_roman(self):
        """Функция переводит римские цифры числа в арабские и возвращает значение арабского числа"""

        arab_num = 0
        for roman_k, arab_v in self.roman_arab_dict.items():
            while self.roman_num.startswith(roman_k):
                arab_num += arab_v
                self.roman_num = self.roman_num[len(roman_k):]
        return arab_num

    def is_palindrome(self):
        """Функция проверяет является ли арабское число палиндромом (True - является, иначе False)"""

        arab_num = str(self.from_roman())
        center_str = len(arab_num) // 2
        if len(arab_num) == 1:
            return True
        elif len(arab_num) % 2 == 0:
            arab_num_end = arab_num[center_str:]
        else:
            arab_num_end = arab_num[center_str + 1:]
        print(arab_num[:center_str])
        print(''.join(reversed(arab_num_end)))
        if arab_num[:center_str] != ''.join(reversed(arab_num_end)):
            return False
        else:
            return True


# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


data = [RomanNums('MMMCCLXIII').from_roman,
        RomanNums('CXXXIV').from_roman,
        RomanNums('LXXXVI').from_roman,
        RomanNums('MCDV').from_roman,
        RomanNums('CMLXXVIII').from_roman,
        RomanNums('MMMCDIV').from_roman,
        RomanNums('CMX').from_roman,
        RomanNums('MMCCCLXXXVIII').from_roman,
        RomanNums('MMVIII').from_roman,
        RomanNums('MCLXXIX').from_roman,
        RomanNums('MMMDCCXCV').from_roman,
        RomanNums('CMLXXXVIII').from_roman,
        RomanNums('CMXCIX').from_roman,
        RomanNums('CDXLIV').from_roman,
        RomanNums('CMXCIX').is_palindrome,
        RomanNums('CDXLIV').is_palindrome,
        RomanNums('MMMCCLXIII').is_palindrome,
        RomanNums('CXXXIV').is_palindrome,
        RomanNums('V').is_palindrome,
        RomanNums('MI').is_palindrome,
        RomanNums('XXX').is_palindrome,
        RomanNums('D').is_palindrome,
        ]

test_data = [3263, 134, 86, 1405, 978, 3404, 910, 2388, 2008, 1179, 3795, 988, 999, 444,
             True, True, False, False, True, True, False, False]

for i, d in enumerate(data):
    assert_error = f'Не прошла проверка для метода {d.__qualname__} экземпляра с атрибутами {d.__self__.__dict__}'
    assert d() == test_data[i], assert_error
    print(f'Набор для метода {d.__qualname__} экземпляра класса с атрибутами {d.__self__.__dict__} прошёл проверку')
print('Всё ок')
