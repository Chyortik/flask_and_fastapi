from threading import Thread
import time
import random

t_sum = 0


def arr_create():
    arr = [random.randint(1, 100) for _ in range(1_000_000)]
    return arr


def thread_sum():
    global t_sum
    for i in arr_create():
        t_sum += i


threads = []
thread_time = time.time()


if __name__ == '__main__':
    t1 = Thread(target=arr_create)
    threads.append(t1)
    t1.start()
    t2 = Thread(target=thread_sum)
    threads.append(t2)
    t2.start()
    for t in threads:
        t.join()
    print(f'Сумма элементов заданного массива = {t_sum} \
               \nВремя выполнения: {(time.time() - thread_time):.2f} секунд\n')
