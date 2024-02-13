import numpy
import requests
from PIL import Image
import matplotlib.pyplot as plt
import pandas as pd


def get_data_from_api():
    url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
    response = requests.get(url)
    data = response.json()
    print("Текущий курс биткоина в USD:", data['bpi']['USD']['rate'])


get_data_from_api()


def manipulate_array():
    array = numpy.arange(10)
    squared_array = numpy.square(array)
    print('Исходный массив ', array)
    print('Квадраты элементов ', squared_array)


manipulate_array()

new_image = Image.new('RGB', (500, 500), 'red')
new_image.save('new_image.jpg')


def process_image():
    img = Image.open('new_image.jpg')
    resized_img = img.resize((200, 200))
    resized_img.save('output_image.png')


process_image()


def visualize_sales(dates, sales):
    plt.plot(dates, sales)
    plt.xlabel('Дата')
    plt.ylabel('Продажи')
    plt.title('Динамика прдаж')
    plt.show()


dates = ['2024-01-01', '2023-01-01', '2022-01-01', '2021-01-01']
sales = [200, 300, 400, 500]

visualize_sales(dates, sales)


def analyze_data(filename):
    df = pd.read_csv(filename)
    print('Статистика по данным из файла ')
    print('Среднее значение', df['value'].mean())
    print('', df['value'].max())
    print('', df['value'].min())


analyze_data('data.csv')
