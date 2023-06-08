# Есть маркер @pytest.mark.id_check(1, 2, 3), нужно вывести на печать, то что в него передано
#
# >>> 1, 2, 3

import pytest


@pytest.fixture
def get_marks(request):
    """Фикстура которая дает доступ к аргументам маркера"""
    marker = request.node.get_closest_marker('id_check')
    return marker


@pytest.mark.id_check(1, 2, 3)
def test(get_marks):
    """Тест к которому применяем фикстуру возврата маркера"""
    print()
    for i in get_marks.args:
        print(i, end=' ')




