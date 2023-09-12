import argparse
import time
import os
import requests

URLS = [
    'https://darstroy-yug.ru/upload/medialibrary/0f9/0f904c4d27a68126350b4b24a25d2e83.jpeg',
    'https://darstroy-yug.ru/upload/medialibrary/890/890d776f938175fec76e349af9f066d5.jpg',
    'https://darstroy-yug.ru/upload/medialibrary/d8e/d8e703d4b39dde03b826726726f98c9c.jpg'
]

start_func_time = time.time()


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('url_list', nargs="*")
    args = parser.parse_args()
    return args.url_list


def img_saver(urls):
    if not os.path.exists('images'):
        os.makedirs('images')
    for url in urls:
        start_time = time.time()
        response = requests.get(url)
        filename = f'{url.split("/")[-1]}'
        with open(f'images/{filename}', 'wb') as f:
            f.write(response.content)
        print(f'Файл {filename} загружен за {(time.time() - start_time):.2f} секунд')


if __name__ == '__main__':
    img_saver(URLS)
    print(f'Время выполнения: {(time.time() - start_func_time):.2f} секунд')
