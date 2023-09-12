from multiprocessing import Process, Value
import time
import random

p_sum = Value('i', 0)


def arr_create():
    arr = [random.randint(1, 100) for _ in range(1_000_000)]
    return arr


def process_sum(cnt):
    global p_sum
    for i in arr_create():
        with cnt.get_lock():
            p_sum.value += i


process_time = time.time()


if __name__ == '__main__':
    p1 = Process(target=arr_create)
    p2 = Process(target=process_sum(p_sum))
    processes = [p1, p2]
    for p in processes:
        p.start()
    for p in processes:
        p.join()
    print(f'Сумма элементов заданного массива = {p_sum.value} \
                   \nВремя выполнения: {(time.time() - process_time):.2f} секунд\n')
