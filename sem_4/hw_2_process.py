import argparse
from multiprocessing import Process
import os
import time
import requests

URLS = [
    'https://samplelib.com/lib/preview/jpeg/sample-red-400x300.jpg',
    'https://samplelib.com/lib/preview/jpeg/sample-green-400x300.jpg',
    'https://samplelib.com/lib/preview/jpeg/sample-blue-400x300.jpg'
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


processes = []
start_time = time.time()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('url_list', nargs="*")
    args = parser.parse_args()
    # for url in args.url_list: # for args via cmd
    for url in URLS:
        process = Process(target=img_saver, args=(url,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    print(f'Время выполнения: {(time.time() - start_func_time):.2f} секунд')
