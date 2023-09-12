import asyncio
import aiohttp
import time
import argparse
import os

URLS = [
    'https://cdn.fotosklad.ru/unsafe/d307eb3569bf42a782970487291e55ad/image.jpg',
    'https://samplelib.com/lib/preview/jpeg/sample-clouds-400x300.jpg',
    'https://samplelib.com/lib/preview/jpeg/sample-city-park-400x300.jpg'
]

start_func_time = time.time()
if not os.path.exists('images'):
    os.makedirs('images')


async def img_saver(url):
    async with aiohttp.ClientSession() as session:
        start_time = time.time()
        async with session.get(url) as response:
            cont = await response.read()
            filename = f'{url.split("/")[-1]}'
            with open(f'images/{filename}', 'wb') as f:
                f.write(cont)
                print(f'Файл {filename} загружен за {(time.time() - start_time):.2f} секунд')


async def main():
    tasks = []
    parser = argparse.ArgumentParser()
    parser.add_argument('url_list', nargs="*")
    args = parser.parse_args()
    # for url in args.url_list: # for args via cmd
    for url in URLS:
        task = asyncio.ensure_future(img_saver(url))
        tasks.append(task)
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    print(f'Время выполнения: {(time.time() - start_func_time):.2f} секунд')
