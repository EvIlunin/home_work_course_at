import pytest
from datetime import datetime as date
from time import time


@pytest.fixture()
def timer_cls_start_end():
    time_start = date.today().strftime('%H:%M:%S')
    print(f"Время начала теста {time_start}")
    yield
    time_finish = date.today().time().strftime('%H:%M:%S')
    print(f"\nВремя окончания теста {time_finish}")


@pytest.fixture()
def timer_test():
    timer_test_start = time()
    yield
    timer_test_finish = time()
    print(f'Время выполнения теста {timer_test_finish - timer_test_start}\n')
