# Дан файл test_file/task_3.txt можно считать, что это запись покупок в магазине, где указана только цена товара
# В каждой строке файла записана цена товара.
# Покупки (т.е. несколько подряд идущих цен) разделены пустой строкой
# Нужно найти сумму трёх самых дорогих покупок, которые запишутся в переменную three_most_expensive_purchases


# Здесь пишем код
sum_purchases = 0
list_purchases = []
with open('test_file/task_3.txt', 'r', encoding='utf-8') as file_purchases:
    for i in file_purchases:
        if i == '\n':
            list_purchases.append(sum_purchases)
            sum_purchases = 0
            continue
        sum_purchases += int(i)
three_most_expensive_purchases = sum(sorted(list_purchases)[::-1][0:3])
assert three_most_expensive_purchases == 202346




