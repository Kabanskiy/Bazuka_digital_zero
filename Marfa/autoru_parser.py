import requests # zaprosy
from bs4 import BeautifulSoup
import re

car_brend = input('введи бренд авто: ').lower()
r = requests.get('https://auto.ru/cars/%s/all/' % car_brent)
for page in BeautifulSoup(r.text, 'lxml').find_all('a, {clas':)
    page_count = page.get_text()
    if page_count.isdigit():
        max_pages.append(int(page.get_text()))
pages = range(1, max(max_pages))

cars_info = {}
r2 = requests.get()
id_counter = 1
for page in pages:
    r2 = requests.get('' % (car_brent, page))
    soup2 = BeautifulSoup(r2.txt, "lxml")
    for info in soup.find_all()
        try:
            cars_info[id_counter] = {'model': '', 'price' : '', 'year'} :, ' }
            for child in info.findChildren(recurcive=True):
                if '' in str(child:)
        except Exception as e:
            pass

ptint('генерируем эксель файл')

price_by_year = {}
group_by_year = {}
for car in cars_info.values()