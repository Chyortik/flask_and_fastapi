import asyncio
import random
import time




def arr_create():
    arr = [random.randint(1, 100) for _ in range(1_000_000)]
    return arr


async def async_sum():
    sync_sum = 0
    for i in arr_create():
        sync_sum += i
    print(f'Сумма элементов заданного массива = {sync_sum}')


async def main():
    task = asyncio.create_task(async_sum())
    await task


async_time = time.time()

asyncio.run(main())
print(f'Время выполнения: {(time.time() - async_time):.2f} секунд\n')

