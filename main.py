import random
import datetime
import time
import telebot
import re
import lxml
import requests
from bs4 import BeautifulSoup

TOKEN = '1261421852:AAH2vZM59fLQ9PYvJj45VvgcGdDhJ4xNnrs'

bot = telebot.TeleBot(TOKEN)
@bot.message_handler(content_types = ['text'])
def func(message):
    #bot.send_message(message.chat.id, message.text)
    weather_func(message, bot)

def weather_func(mes, tbot):
    if re.search(r'\bпогода\b', mes.text.lower()) or re.search(r'\bпогоду\b', mes.text.lower()):
        if re.search(r'\bзавтра\b', mes.text.lower()):
            wait_func(tbot, mes)
            
            date_month = datetime.datetime.today().strftime("%m")
            date_day = datetime.datetime.today().strftime("%d") 
            url = 'https://meteo.ua/1001/gogolevo/tomorrow'
            url_two = 'https://sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D0%B3%D0%BE%D0%B3%D0%BE%D0%BB%D0%B5%D0%B2%D0%BE/2021-'+ str(date_month) +'-'+ str(date_day)
            response = requests.get(url)
            response_two = requests.get(url_two)
            soup = BeautifulSoup(response.text, 'lxml')
            soup_two = BeautifulSoup(response_two.text, 'lxml')
            temp = soup.find_all('span', class_='wwt_max')
            temp_text = str(temp[2].text[63:])
            desc = soup_two.find('div', class_='description')
            max_temp = '0'
            min_temp = '0'

            tbot.send_message(mes.chat.id, "Я думаю температура будет в районе " + temp_text + "\n\n" + desc.text[2:])
        elif re.search(r'\bсейчас\b', mes.text.lower()) or re.search(r'\bсегодня\b', mes.text.lower()):
            wait_func(tbot, mes)

            url = 'https://sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D0%B3%D0%BE%D0%B3%D0%BE%D0%BB%D0%B5%D0%B2%D0%BE'
            url_two = 'https://weather.com/weather/today/l/49.92,33.83?par=google&temp=c'
            response = requests.get(url)
            response_two = requests.get(url_two)
            soup = BeautifulSoup(response.text, 'lxml')
            soup_two = BeautifulSoup(response_two.text, 'lxml')
            temp = soup.find('p', class_='today-temp')
            desc = soup.find('div', class_='description')
            max_min = soup_two.find('div', class_='WeatherDetailsListItem--wxData--23DP5')
            max_min_arr = max_min.text.split('/')
            max_temp = max_min_arr[1]
            min_temp = max_min_arr[0]

            tbot.send_message(mes.chat.id, "Температура за бортом "+ temp.text +".\n\n" + "Минимальная температура " + max_temp + "\nМаксимальная " + min_temp + "\n\n" + desc.text[2:])
        else:
            tbot.send_message(mes.chat.id, 'Я не доконца поняла ваш запрос')
    else:
        tbot.send_message(mes.chat.id, 'No')

def wait_func(tbot, mes):
    rand_numb = random.randint(1, 8)
    if rand_numb == 1:
        tbot.send_message(mes.chat.id, "Подождите секундочку")
    elif rand_numb == 2:
        tbot.send_message(mes.chat.id, "В обработке")
    elif rand_numb == 3:
        tbot.send_message(mes.chat.id, "Обрабатываю")
    elif rand_numb == 4:
        tbot.send_message(mes.chat.id, "Раздумываю над вопросом")
    elif rand_numb == 5:
        tbot.send_message(mes.chat.id, "~Тяжело вздыхает~")
    elif rand_numb == 6:
        tbot.send_message(mes.chat.id, "Дай подумать")
    elif rand_numb == 7:
        tbot.send_message(mes.chat.id, "Хороший вопрос")
    else:
        tbot.send_message(mes.chat.id, "Я не знаю что сказать Х)")

def loop():
    while 1:
        bot.send_message(message.chat.id, "Sec")
        time.sleep(1)


bot.polling(none_stop=True)