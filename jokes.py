import requests
from bs4 import BeautifulSoup as b

URL = 'https://www.anekdot.ru/last/good/'

def parser(url):
    r = requests.get(url)
#отвечает ли сервер (200-good)
# print(r.status_code)

    soup = b(r.text, "html.parser")
#выкачиваем коллекцию анекдотов с сайта

    anekdots = soup.find_all('div', class_='text')  #текст будет с тэгами
    return [c.text for c in anekdots]   #очищаем от тегов
# clear_anekdots = [c.text for c in anekdots]   #очищаем от тегов
# print(clear_anekdots)
