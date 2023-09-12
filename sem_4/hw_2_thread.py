import argparse
from threading import Thread
import time
import os
import requests

URLS = [
    'https://primorye24.ru/uploads/media/news/0005/05/thumb_404918_news_xl_crop.jpeg',
    'https://primorye24.ru/uploads/media/news/0005/15/thumb_414564_news_m.jpeg',
    'https://primorye24.ru/uploads/media/news/0005/15/thumb_414566_news_m.jpeg'
]

start_func_time = time.time()
if not os.path.exists('images'):
    os.makedirs('images')


def img_saver(url):
    response = requests.get(url)
    filename = f'{url.split("/")[-1]}'
    with open(f'images/{filename}', 'wb') as f:
        f.write(response.content)
        print(f'Файл {filename} загружен за {(time.time() - start_time):.2f} секунд')


threads = []
start_time = time.time()


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('url_list', nargs="*")
    args = parser.parse_args()
    return args.url_list


for url in URLS:
    thread = Thread(target=img_saver, args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print(f'Время выполнения: {(time.time() - start_func_time):.2f} секунд')
