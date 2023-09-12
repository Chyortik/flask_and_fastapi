import random
import time


def arr_create():
    arr = [random.randint(1, 100) for _ in range(1_000_000)]
    return arr


def sync_sum():
    sync_time = time.time()
    sync_sum_val = 0
    for i in arr_create():
        sync_sum_val += i
    return f'Сумма элементов заданного массива = {sync_sum_val} \
           \nВремя выполнения: {(time.time() - sync_time):.2f} секунд\n'


print(sync_sum())
