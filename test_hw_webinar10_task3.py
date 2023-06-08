# Из набора тестов задания task_2 создайте один тест с параметрами, используя @pytest.mark.parametrize
# Промаркируйте 1 параметр из выборки как smokе, а 1 набор данных скипните

import pytest
import test_hw_webinar10_task2 as test_case


@pytest.mark.parametrize('test', (
    pytest.param(test_case.test_1(), marks=pytest.mark.smoke),
    test_case.test_2(),
    pytest.param(test_case.test_3_my_tree(), marks=pytest.mark.skip('bad case')),
    test_case.test_4_my(),
    test_case.test_5_zero_division()
), ids=['test_1', 'test_2', 'test_3_my_tree', 'test_my', 'test_5_zero_division'])
def test_all(test):
    pass


def all_division(*arg1):
    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division
