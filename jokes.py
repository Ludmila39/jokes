import requests
import random
import telebot
from bs4 import BeautifulSoup as b




URL = 'https://www.anekdot.ru/last/good/'
API_KEY = '5308355497:AAH_xkAKHFfVpEeVcUajEq9alOzczFuXBrE'


def parser(url):
    r = requests.get(url)
    # отвечает ли сервер (200-good)
    # print(r.status_code)

    soup = b(r.text, "html.parser")
    # выкачиваем коллекцию анекдотов с сайта

    anekdots = soup.find_all('div', class_='text')  # текст будет с тэгами
    return [c.text for c in anekdots]  # очищаем от тегов


# clear_anekdots = [c.text for c in anekdots]   #очищаем от тегов
# print(clear_anekdots)

list_of_jokes = parser(URL)
random.shuffle(list_of_jokes)

bot = telebot.TeleBot(API_KEY)
@bot.message_handler(commands =['start'])

def hello (message):
    bot.send_message(message.chat.id, 'Hello, input another number to laugh!')

bot.polling()


