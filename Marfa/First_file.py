import requests # zaprosy
from bs4 import BeautifulSoup
import pandas # для данных библиотека
cars_and_count = {} # для хранения пар
r = requests.get('https://auto.ru/') # perem-ya c zaprosom
soup = BeautifulSoup(r.text, 'lxml') # здесь получаем разметку в формате
for car in soup.find_all('a', {'index_mark__items'}): # ищем здесь все машины
    brent_name = ''
    brent_count = 0
    for child in car.children:
        if '' in str(child):
            brent_name = child.get_text().encode(r.encoding).decode()
        elif 'IndexMarks__item' in str(child):
            brent_count = child.get_text()
    if brent_name not in cars_and_count or brent_count > cars_and_coun[brent_name]
        cars_and_count[brent_name] = brent_count
print(cars_and_count)

pandas.DataFrame(data=cars_and_count, index=[0]).to_excel