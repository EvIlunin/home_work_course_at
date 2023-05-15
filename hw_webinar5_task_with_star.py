# Напишите функцию to_roman, которая преобразуют арабское число (val) в римское (roman_str).
#
# Современные римские цифры записываются, выражая каждую цифру отдельно,
# начиная с самой левой цифры и пропуская цифру со значением нуля.
# Римскими цифрами 1990 отображается: 1000=М, 900=СМ, 90=ХС; в результате MCMXC.
# 2023 записывается как 2000=MM, 20=XX, 3=III; или MMXXIII.
# В 1666 используется каждый римский символ в порядке убывания: MDCLXVI.
#
# Например (Ввод --> Вывод) :
# 2008 --> MMVIII


def to_roman(val):
    roman_str = ''
    roman_num_dict = {'1000': ["", "M", "MM", "MMM", "MMMM", 'MV', 'V', 'VM', 'VMM', 'VMMM', 'MX'],
                      '100': ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"],
                      '10': ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"],
                      '1': ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"],
                      }
    for rank in roman_num_dict.keys():
        if val // int(rank) > 0:
            roman_str += roman_num_dict[rank][val // int(rank)]
        else:
            continue
        val = val % int(rank)
    return roman_str

# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


data = [1133, 2224, 1938, 1817, 2505, 391, 3743, 1634, 699, 1666, 1494, 1444]

test_data = [
    "MCXXXIII", "MMCCXXIV", "MCMXXXVIII", "MDCCCXVII", "MMDV", "CCCXCI", 'MMMDCCXLIII', 'MDCXXXIV', 'DCXCIX', 'MDCLXVI',
    'MCDXCIV', 'MCDXLIV']


for i, d in enumerate(data):
    assert to_roman(d) == test_data[i], f'С набором {d} есть ошибка, не проходит проверку'
    print(f'Тестовый набор {d} прошёл проверку')
print('Всё ок')