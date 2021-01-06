import logging

import requests as req
from bs4 import BeautifulSoup as bs
import time
import constants, os, re
import telebot
from telebot import types

bot = telebot.TeleBot('1363554818:AAGqIvC4_M6n3ZCnn90AA12edNq1rax_Flo')
def inline(message):
    bot.send_message(message.chat.id,"Цену какой акции ,{0.first_name}, Вы желаете посмотреть?".format(message.from_user),parse_mode="html",)
    key = types.InlineKeyboardMarkup()
    but1 = types.InlineKeyboardButton(text="Газпром", callback_data="Газпром")
    but2 = types.InlineKeyboardButton(text="Сбербанк", callback_data="Сбербанк")
    but3 = types.InlineKeyboardButton(text="Татнефть", callback_data="Татнефть")
    but4 = types.InlineKeyboardButton(text="Роснефть", callback_data="Роснефть")
    but5 = types.InlineKeyboardButton(text="Яндекс", callback_data="Яндекс")
    but6 = types.InlineKeyboardButton(text="Норникель", callback_data="Норникель")
    but7 = types.InlineKeyboardButton(text="Мосбиржа", callback_data="Мосбиржа")
    but8 = types.InlineKeyboardButton(text="НКНХ", callback_data="НКНХ")
    but9 = types.InlineKeyboardButton(text="МТС", callback_data="МТС")
    but10 = types.InlineKeyboardButton(text="НЛМК", callback_data="НЛМК")
    key.add(but1, but2, but3, but4, but5, but6, but7, but8, but9, but10)
    bot.send_message(message.chat.id,"Выберите акцию" ,reply_markup=key)



def stock(company):
    r = req.get('https://www.finam.ru/quote/moex-akcii/')


    soup = bs(r.text, 'lxml')
    price_s = soup.findAll('span', {'class': 'PriceInformation__price--26G'})
    price_s = price_s[0].text


@bot.message_handler(commands=["start"])
@bot.message_handler(content_types=['text'])
def send_text(message):
     if message.text == 'Привет':
         bot.send_message(message.chat.id, 'Привет, Артём')
     elif message.text == 'Пока':
         bot.send_message(message.chat.id, 'Пока, Артём')
     elif message.text == 'Цена':
         bot.send_message(message.chat.id, 'Сейчас появится таблица с данными')
         time.sleep(2)
         inline(message)


@bot.callback_query_handler(func=lambda price: True)
def price_stocks(call):
    key_main = types.InlineKeyboardMarkup()
    but1 = types.InlineKeyboardButton(text="Газпром", callback_data="Газпром")
    but2 = types.InlineKeyboardButton(text="Сбербанк", callback_data="Сбербанк")
    but3 = types.InlineKeyboardButton(text="Татнефть", callback_data="Татнефть")
    but4 = types.InlineKeyboardButton(text="Роснефть", callback_data="Роснефть")
    but5 = types.InlineKeyboardButton(text="Яндекс", callback_data="Яндекс")
    but6 = types.InlineKeyboardButton(text="Норникель", callback_data="Норникель")
    but7 = types.InlineKeyboardButton(text="Мосбиржа", callback_data="Мосбиржа")
    but8 = types.InlineKeyboardButton(text="НКНХ", callback_data="НКНХ")
    but9 = types.InlineKeyboardButton(text="МТС", callback_data="МТС")
    but10 = types.InlineKeyboardButton(text="НЛМК", callback_data="НЛМК")
    key_main.add(but1, but2, but3, but4, but5, but6, but7, but8, but9, but10)
    if call.data == "Газпром":
        r = req.get('https://www.finam.ru/quote/moex-akcii/gazprom/')
        soup = bs(r.text, 'lxml')
        price_s = soup.findAll('span', {'class': 'PriceInformation__price--26G'})
        price_s = price_s[0].text
        print(price_s)
        bot.send_message(call.message.chat.id, "Цена Газпрома: {0}".format(price_s), reply_markup=key_main)
        # bot.send_message(price_s.chat.id, 'Через 20 секунд вы узнаете цену акций')
        #bot.send_message(message.chat.id, price1, 'Цена выросла')
        #key1=types.InlineKeyboardMarkup()
        #k1=types.InlineKeyboardButton(text="Узнать цену", callback_data="price")
        #k2=types.InlineKeyboardButton(text="Back",callback_data="menu")
        #key1.add(k1,k2)
        #bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message.id,text="Газпром",reply_markup=key1)


    if call.data == "Сбербанк":
        r = req.get('https://www.finam.ru/quote/moex-akcii/sberbank-pref')
        soup = bs(r.text, 'lxml')
        price_s = soup.findAll('span', {'class': 'PriceInformation__price--26G'})
        price_s = price_s[0].text
        print(price_s)
        bot.send_message(call.message.chat.id, "Цена Сбербанка: {0}".format(price_s),reply_markup=key_main)
    if call.data == "Татнефть":
        r = req.get('https://www.finam.ru/quote/moex-akcii/tatneft-pref/')
        soup = bs(r.text, 'lxml')
        price_s = soup.findAll('span', {'class': 'PriceInformation__price--26G'})
        price_s = price_s[0].text
        print(price_s)
        bot.send_message(call.message.chat.id,"Цена акции Татнефть: {0}".format(price_s), reply_markup=key_main)
    if call.data == "Роснефть":
        r = req.get('https://www.finam.ru/quote/moex-akcii/rosneft/')
        soup = bs(r.text, 'lxml')
        price_s = soup.findAll('span', {'class': 'PriceInformation__price--26G'})
        price_s = price_s[0].text
        print(price_s)
        bot.send_message(call.message.chat.id,"Цена акции Роснефть: {0}".format(price_s), reply_markup=key_main)
    if call.data == "Яндекс":
        r = req.get('https://www.finam.ru/quote/moex-akcii/pllc-yandex-n-v/')
        soup = bs(r.text, 'lxml')
        price_s = soup.findAll('span', {'class': 'PriceInformation__price--26G'})
        price_s = price_s[0].text
        print(price_s)
        bot.send_message(call.message.chat.id,"Цена акции Яндекс: {0}".format(price_s), reply_markup=key_main)
    if call.data == "Норникель":
        r = req.get('https://www.finam.ru/quote/moex-akcii/nornickel-gmk/')
        soup = bs(r.text, 'lxml')
        price_s = soup.findAll('span', {'class': 'PriceInformation__price--26G'})
        price_s = price_s[0].text
        print(price_s)
        bot.send_message(call.message.chat.id,"Цена акции Норникель: {0}".format(price_s), reply_markup=key_main)
    if call.data == "Мосбиржа":
        r = req.get('https://www.finam.ru/quote/moex-akcii/moscowexchange/')
        soup = bs(r.text, 'lxml')
        price_s = soup.findAll('span', {'class': 'PriceInformation__price--26G'})
        price_s = price_s[0].text
        print(price_s)
        bot.send_message(call.message.chat.id,"Цена акции Мосбиржи: {0}".format(price_s), reply_markup=key_main)
    if call.data == "НКНХ":
        r = req.get('https://www.finam.ru/quote/moex-akcii/niznekamskneftekhim-pref/')
        soup = bs(r.text, 'lxml')
        price_s = soup.findAll('span', {'class': 'PriceInformation__price--26G'})
        price_s = price_s[0].text
        print(price_s)
        bot.send_message(call.message.chat.id,"Цена акции НКНХ: {0}".format(price_s), reply_markup=key_main)
    if call.data == "МТС":
        r = req.get('https://www.finam.ru/quote/moex-akcii/mts/')
        soup = bs(r.text, 'lxml')
        price_s = soup.findAll('span', {'class': 'PriceInformation__price--26G'})
        price_s = price_s[0].text
        print(price_s)
        bot.send_message(call.message.chat.id,"Цена акции МТС: {0}".format(price_s), reply_markup=key_main)
    if call.data == "НЛМК":
        r = req.get('https://www.finam.ru/quote/moex-akcii/nlmk-ao/')
        soup = bs(r.text, 'lxml')
        price_s = soup.findAll('span', {'class': 'PriceInformation__price--26G'})
        price_s = price_s[0].text
        print(price_s)
        bot.send_message(call.message.chat.id,"Цена акции НЛМК: {0}".format(price_s), reply_markup=key_main)


# def start_message(message):
#     bot.send_message(message.chat.id, 'Привет, ты написал мне /start', reply_markup=keyboard1)
#
#

# bot.polling(none_stop=True)
# <span class="PriceInformation__price--26G">183,46 RUB</span>
bot.polling(none_stop=True)
