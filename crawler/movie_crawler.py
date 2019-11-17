#-*- coding: utf-8 -*-

import requests
import telegram
from bs4 import BeautifulSoup

bot = telegram.Bot(token='999630453:AAGjO2fijWMeWmCYMt6kFw5-C6IKJ8UINtY')
url = 'http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=01&theatercode=0013&date=20191123'
html = requests.get(url)

soup = BeautifulSoup(html.text, 'html.parser')
imax = soup.select_one('span.imax')
if (imax) :
    imax = imax.find_parent('div', class_='col-times')
    title = imax.select_one('div.info-movie > a > strong').text.strip()
    bot.sendMessage(chat_id=967963705, text=title + ' IMAX 예매가 열렸습니다.')
    #print(title + '의 IMAX 예매가 열렸습니다.')
else :
    bot.sendMessage(chat_id=967963705, text='IMAX 예매가 열리지 않았습니다.')

