# Напишите класс Segment
# Для его инициализации нужно два кортежа с координатами точек (x1, y1), (x2, y2)
# Реализуйте методы классы:
# 1. length, который возвращает длину нашего отрезка, с округлением до 2 знаков после запятой
# 2. x_axis_intersection, который возвращает True, если отрезок пересекает ось абцисс, иначе False
# 3. y_axis_intersection, который возвращает True, если отрезок пересекает ось ординат, иначе False
# Например (Ввод --> Вывод) :
# Segment((2, 3), (4, 5)).length() --> 2.83
# Segment((-2, -3), (4, 5)).x_axis_intersection() --> True
# Segment((-2, -3), (4, -5)).y_axis_intersection() --> False

# Здесь пишем код
class Segment:
    """Класс к заданию 1 вебинара 7 с методами определения длинны отрезка и пересечения этим отрезком осей X/Y"""

    def __init__(self, dot1: tuple, dot2: tuple):
        """Посторение отрезка по двум точкам
        :param dot1: координаты точка 1
        :param dot2: координаты точки 2"""
        self.x1, self.y1, self.x2, self.y2 = dot1[0], dot1[1], dot2[0], dot2[1]

    def length(self):
        """ Метод определения длинны отрезка"""

        length = round(((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2) ** 0.5, 2)
        return length

    def x_axis_intersection(self):
        """Метод определяет пересечение отрезка с ось X"""

        if self.x1 >= 0 >= self.x2 or self.x2 >= 0 >= self.x1:
            return True
        else:
            return False

    def y_axis_intersection(self):
        """Метод определяет пересечение отрезка с ось Y"""

        if self.y1 >= 0 >= self.y2 or self.y2 >= 0 >= self.y1:
            return True
        else:
            return False

# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


data = [Segment((2, 3), (4, 5)).length,
        Segment((1, 1), (1, 8)).length,
        Segment((0, 0), (0, 1)).length,
        Segment((15, 1), (18, 8)).length,
        Segment((-2, -3), (4, 5)).x_axis_intersection,
        Segment((-2, -3), (-4, -2)).x_axis_intersection,
        Segment((0, -3), (4, 5)).x_axis_intersection,
        Segment((2, 3), (4, 5)).y_axis_intersection,
        Segment((-2, -3), (4, 5)).y_axis_intersection,
        Segment((-2, 3), (4, 0)).y_axis_intersection
        ]


test_data = [2.83, 7.0, 1.0, 7.62, True, False, True, False, True, True]

for i, d in enumerate(data):
    assert_error = f'Не прошла проверка для метода {d.__qualname__} экземпляра с атрибутами {d.__self__.__dict__}'
    assert d() == test_data[i], assert_error
    print(f'Набор для метода {d.__qualname__} экземпляра класса с атрибутами {d.__self__.__dict__} прошёл проверку')
print('Всё ок')