# Создайте класс с тестами и напишите фикстуры в conftest.py:
# 1) Фикстуру для класса и используйте её. Например, печать времени начала выполнения класса с тестами и окончания
# 2) Фикстуру для конкретного теста и используйте её не для всех тестов. Например, время выполнения теста.

import pytest
import test_hw_webinar10_task2 as test_case
import time


@pytest.mark.usefixtures('timer_cls_start_end')
class TestFixture:
    """Класс для проверки задания 4 работу с фикстурами"""

    @pytest.mark.usefixtures('timer_test')
    @pytest.mark.parametrize('test', (
            pytest.param(test_case.test_1(), marks=pytest.mark.smoke),
            test_case.test_2(),
            pytest.param(test_case.test_3_my_tree()),
    ), ids=['test_1', 'test_2', 'test_3_my_tree'])
    def test_1(self, test, timer_test):
        """Тест который делает ничего =)"""
        time.sleep(1)
        pass


