import requests
from bs4 import BeautifulSoup as b

URL = 'https://www.anekdot.ru/last/good/'
r = requests.get(URL)
print(r.status_code)  #отвечает ли сервер
