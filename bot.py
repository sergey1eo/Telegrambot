import telebot
import urllib.request
import lxml.html
import requests
from lxml import etree
from bs4 import BeautifulSoup
from telebot import types
from selenium import webdriver
import configparser




def p_fun2():
    url = 'https://tourism.rostov-gorod.ru/attractions/239/5071/'
    response = requests.get(url)
    strar = ''
    soup = BeautifulSoup(response.text, 'lxml')
    quotes = soup.find_all('div', class_='textblock')
    for i in range(0, len(quotes)):
        strar += quotes[i].text
    return strar

def p_fun3():
    url = 'https://tourism.rostov-gorod.ru/attractions/239/5148/'
    response = requests.get(url)
    strar = ''
    soup = BeautifulSoup(response.text, 'lxml')
    quotes = soup.find_all('div', class_='textblock')
    for i in range(0, len(quotes)):
        strar += quotes[i].text
    return strar

def p_fun4():
    url = 'https://tourism.rostov-gorod.ru/attractions/239/5154/'
    response = requests.get(url)
    strar = ''
    soup = BeautifulSoup(response.text, 'lxml')
    quotes = soup.find_all('div', class_='textblock')
    for i in range(0, len(quotes)):
        strar += quotes[i].text
    return strar

def p_fun5():
    url = 'https://tourism.rostov-gorod.ru/attractions/239/5217/'
    response = requests.get(url)
    strar = ''
    soup = BeautifulSoup(response.text, 'lxml')
    quotes = soup.find_all('div', class_='textblock')
    for i in range(0, len(quotes)):
        strar += quotes[i].text
    return strar

def p_fun6():
    url = 'https://tourism.rostov-gorod.ru/attractions/239/5218/'
    response = requests.get(url)
    strar = ''
    soup = BeautifulSoup(response.text, 'lxml')
    quotes = soup.find_all('div', class_='textblock')
    for i in range(0, len(quotes)):
        strar += quotes[i].text
    return strar

def p_fun7():
    url = 'https://tourism.rostov-gorod.ru/attractions/239/9000/'
    response = requests.get(url)
    strar = ''
    soup = BeautifulSoup(response.text, 'lxml')
    quotes = soup.find_all('div', class_='textblock')
    for i in range(0, len(quotes)):
        strar += quotes[i].text
    return strar



bot = telebot.TeleBot('5122461139:AAFlY_dzSDOkfAudveIqySp1aO6nERNJDO0')

# Назначенин кнопок (меню)###############
@bot.message_handler(commands=['start'])
def start(message):
       markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
       bot.send_message(message.chat.id,'Привет, {0.first_name}! Чем могу помочь?'.format(message.from_user), reply_markup=markup )
       musey = types.KeyboardButton('СПОРТИВНЫЕ СООРУЖЕНИЯ')
       park = types.KeyboardButton('Парки и Скверы')
       shop = types.KeyboardButton('Торговые центры')
       kino = types.KeyboardButton('Кинотеатры')
       zoopark = types.KeyboardButton('ЦИРК, ДЕЛЬФИНАРИЙ, ЗООПАРК')
       markup.add(park, musey, kino,shop,zoopark)
       bot.send_message(message.chat.id, 'Вот для тебя варианты)', reply_markup=markup)


# Действие кнопок ######################

@bot.message_handler(content_types=['text'])
def fun1(message):
    if (message.text == 'Парки и Скверы'):
        bot.send_message(message.chat.id,'Начинаю поиск...')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        p1 = types.KeyboardButton('ПОКРОВСКИЙ СКВЕР')
        p2 = types.KeyboardButton('ПАРК ИМ. М. ГОРЬКОГО')
        p3 = types.KeyboardButton('УЛИЦА ПУШКИНСКАЯ')
        p4 = types.KeyboardButton('ДЕТСКИЙ ПАРК ИМ. ВИТИ ЧЕРЕВИЧКИНА')
        p5 = types.KeyboardButton('ПАРК КУЛЬТУРЫ И ОТДЫХА "1 МАЯ"')
        p6 = types.KeyboardButton('ПАРК "СКАЗКА"')
        p7 = types.KeyboardButton('Меню')
        markup.add(p1, p2, p3, p4, p5, p6,p7)
        bot.send_message(message.chat.id, "Куда хочешь пойти?", reply_markup=markup)

    elif(message.text == 'Меню'):
        bot.send_message(message.text.id,fun1())



    if(message.text=='ПАРК ИМ. М. ГОРЬКОГО'):
            bot.send_message(message.chat.id, '.........................................................................')
            bot.send_message(message.chat.id, 'ПАРК ИМ. М. ГОРЬКОГО')
            bot.send_photo(message.chat.id, photo='https://tourism.rostov-gorod.ru/upload/resize_cache/iblock/42d/600_400_1/42d406eaf78cd505e7d25dd9245267d6.jpg')
            bot.send_message(message.chat.id, p_fun3())

            bot.send_location(message.from_user.id, 47.22236,39.709785)

            bot.send_message(message.chat.id, '.........................................................................')

    elif(message.text == 'ПОКРОВСКИЙ СКВЕР'):
            bot.send_message(message.chat.id, '.........................................................................')
            bot.send_message(message.chat.id, 'ПОКРОВСКИЙ СКВЕР')
            bot.send_photo(message.chat.id, photo='https://tourism.rostov-gorod.ru/upload/resize_cache/iblock/31e/600_400_1/31ea276da5aedb05fd64e49d984f81a0.png')
            bot.send_message(message.chat.id, p_fun2())

            bot.send_location(message.from_user.id, 47.225829,39.731955)

            bot.send_message(message.chat.id, '.........................................................................')

    elif(message.text == 'УЛИЦА ПУШКИНСКАЯ'):
            bot.send_message(message.chat.id, '.........................................................................')
            bot.send_message(message.chat.id, 'УЛИЦА ПУШКИНСКАЯ')
            bot.send_photo(message.chat.id,  photo='https://tourism.rostov-gorod.ru/upload/resize_cache/iblock/1b7/600_400_1/1b7ef0100bb0a65107166fa209f0b164.jpg')
            bot.send_message(message.chat.id, p_fun4())

            bot.send_location(message.from_user.id, 47.225903,39.719046)

            bot.send_message(message.chat.id, '.........................................................................')

    elif (message.text == 'ДЕТСКИЙ ПАРК ИМ. ВИТИ ЧЕРЕВИЧКИНА'):
        bot.send_message(message.chat.id, '.........................................................................')
        bot.send_message(message.chat.id, 'ДЕТСКИЙ ПАРК ИМ. ВИТИ ЧЕРЕВИЧКИНА')
        bot.send_photo(message.chat.id,photo='https://tourism.rostov-gorod.ru/upload/resize_cache/iblock/97e/600_400_1/97e273b9bde56190b15af137c0aa0229.jpg')
        bot.send_message(message.chat.id, p_fun5())

        bot.send_location(message.from_user.id, 47.227267,39.749508)

        bot.send_message(message.chat.id, '.........................................................................')

    elif (message.text == 'ПАРК КУЛЬТУРЫ И ОТДЫХА "1 МАЯ"'):
        bot.send_message(message.chat.id, '.........................................................................')
        bot.send_message(message.chat.id, 'ПАРК КУЛЬТУРЫ И ОТДЫХА "1 МАЯ"')
        bot.send_photo(message.chat.id,photo='https://tourism.rostov-gorod.ru/upload/resize_cache/iblock/ca1/600_400_1/ca11f1b02d86b8e8cbf3069d496c18e4.jpg')
        bot.send_message(message.chat.id, p_fun6())

        bot.send_location(message.from_user.id, 47.222078,39.720358)

        bot.send_message(message.chat.id, '.........................................................................')

    elif (message.text == 'ПАРК "СКАЗКА"'):
        bot.send_message(message.chat.id, '.........................................................................')
        bot.send_message(message.chat.id, 'ПАРК "СКАЗКА"')
        bot.send_photo(message.chat.id,photo='https://tourism.rostov-gorod.ru/upload/resize_cache/iblock/c1b/600_400_1/c1bdb8f85a9221bfff3aba196d178969.jpg')
        bot.send_message(message.chat.id, p_fun7())

        bot.send_location(message.from_user.id, 47.208368,39.625136)

    #elif(message.text == 'Меню') :
      #  bot.send_message(message.chat.id,fun_menu)





    elif(message.text == 'СПОРТИВНЫЕ СООРУЖЕНИЯ'):
        bot.send_message(message.chat.id, 'Начинаю поиск...')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        p1 = types.KeyboardButton('СТАДИОН ОЛИМП- 2')
        p2 = types.KeyboardButton('ГРЕБНОЙ КАНАЛ "ДОН"')
        p3 = types.KeyboardButton('ЛЕДОВЫЙ ДВОРЕЦ "ICE ARENA"')
        p4 = types.KeyboardButton('СТАДИОН "РОСТОВ-АРЕНА"')
        p5 = types.KeyboardButton('СТАДИОН "ДИНАМО"')
        p6 = types.KeyboardButton('СТАДИОН "ЛОКОМОТИВ"')
        p7 = types.KeyboardButton('Меню')
        markup.add(p1, p2, p3, p4, p5, p6, p7)
        bot.send_message(message.chat.id, "Куда хочешь пойти?", reply_markup=markup)

    elif(message.text == 'СТАДИОН ОЛИМП- 2'):
        bot.send_message(message.chat.id, '.........................................................................')

        def s_fun1():
            url = 'https://tourism.rostov-gorod.ru/attractions/244/5083/'
            response = requests.get(url)
            strar = ''
            soup = BeautifulSoup(response.text, 'lxml')
            quotes = soup.find_all('div', class_='textblock')
            for i in range(0, len(quotes)):
                strar += quotes[i].text
            return strar

        bot.send_message(message.chat.id, 'СТАДИОН ОЛИМП- 2')
        bot.send_photo(message.chat.id,photo='https://tourism.rostov-gorod.ru/upload/resize_cache/iblock/6de/600_400_1/6de9475590bb74e7bc2828151743bf98.jpg')
        bot.send_message(message.chat.id, s_fun1())

        bot.send_location(message.from_user.id, 47.243090, 39.760790)

        bot.send_message(message.chat.id, '.........................................................................')



    elif(message.text == 'ГРЕБНОЙ КАНАЛ "ДОН"'):
        bot.send_message(message.chat.id, '.........................................................................')

        def s_fun2():
            url = 'https://tourism.rostov-gorod.ru/attractions/244/5202/'
            response = requests.get(url)
            strar = ''
            soup = BeautifulSoup(response.text, 'lxml')
            quotes = soup.find_all('div', class_='textblock')
            for i in range(0, len(quotes)):
                strar += quotes[i].text
            return strar

        bot.send_message(message.chat.id, 'ГРЕБНОЙ КАНАЛ "ДОН"')
        bot.send_photo(message.chat.id, photo='https://tourism.rostov-gorod.ru/upload/resize_cache/iblock/d35/600_400_1/d3559f5ab5bbb38e3dd8c6bf0d0cc012.jpg')
        bot.send_message(message.chat.id, s_fun2())

        bot.send_location(message.from_user.id, 47.236355, 39.487610)

        bot.send_message(message.chat.id, '.........................................................................')

    elif(message.text == 'ЛЕДОВЫЙ ДВОРЕЦ "ICE ARENA"'):
        bot.send_message(message.chat.id, '.........................................................................')

        def s_fun3():
            url = 'https://tourism.rostov-gorod.ru/attractions/244/5305/'
            response = requests.get(url)
            strar = ''
            soup = BeautifulSoup(response.text, 'lxml')
            quotes = soup.find_all('div', class_='textblock')
            for i in range(0, len(quotes)):
                strar += quotes[i].text
            return strar

        bot.send_message(message.chat.id, 'ЛЕДОВЫЙ ДВОРЕЦ "ICE ARENA"')
        bot.send_photo(message.chat.id, photo='https://tourism.rostov-gorod.ru/upload/resize_cache/iblock/3f6/600_400_1/3f63a9857cd1fb65060977ac506ae4eb.jpg')
        bot.send_message(message.chat.id, s_fun3())

        bot.send_location(message.from_user.id, 47.208778, 39.627589)

        bot.send_message(message.chat.id, '.........................................................................')

    elif(message.text == 'СТАДИОН "РОСТОВ-АРЕНА"'):
        bot.send_message(message.chat.id, '.........................................................................')

        def s_fun4():
            url = 'https://tourism.rostov-gorod.ru/attractions/244/8897/'
            response = requests.get(url)
            strar = ''
            soup = BeautifulSoup(response.text, 'lxml')
            quotes = soup.find_all('div', class_='textblock')
            for i in range(0, len(quotes)):
                strar += quotes[i].text
            return strar

        bot.send_message(message.chat.id, 'СТАДИОН "РОСТОВ-АРЕНА"')
        bot.send_photo(message.chat.id, photo='https://tourism.rostov-gorod.ru/upload/resize_cache/iblock/029/600_400_1/02984276f9518c7b56dda724797387c8.png')
        bot.send_message(message.chat.id, s_fun4())

        bot.send_location(message.from_user.id, 47.209380, 39.737890)

        bot.send_message(message.chat.id, '.........................................................................')

    elif (message.text == 'СТАДИОН "ДИНАМО"'):
        bot.send_message(message.chat.id, '.........................................................................')

        def s_fun5():
            url = 'https://tourism.rostov-gorod.ru/attractions/244/9046/'
            response = requests.get(url)
            strar = ''
            soup = BeautifulSoup(response.text, 'lxml')
            quotes = soup.find_all('div', class_='textblock')
            for i in range(0, len(quotes)):
                strar += quotes[i].text
            return strar

        bot.send_message(message.chat.id, 'СТАДИОН "ДИНАМО"')
        bot.send_photo(message.chat.id, photo='https://tourism.rostov-gorod.ru/upload/resize_cache/iblock/be7/600_400_1/be7042aea63af03d60c5a25381e00882.jpg')
        bot.send_message(message.chat.id, s_fun5())

        bot.send_location(message.from_user.id, 47.237368715044, 39.715209777158)

        bot.send_message(message.chat.id, '.........................................................................')


    elif (message.text == 'СТАДИОН "ЛОКОМОТИВ"'):
        bot.send_message(message.chat.id, '.........................................................................')

        def s_fun6():
            url = 'https://tourism.rostov-gorod.ru/attractions/244/9047/'
            response = requests.get(url)
            strar = ''
            soup = BeautifulSoup(response.text, 'lxml')
            quotes = soup.find_all('div', class_='textblock')
            for i in range(0, len(quotes)):
                strar += quotes[i].text
            return strar

        bot.send_message(message.chat.id, 'СТАДИОН "ЛОКОМОТИВ"')
        bot.send_photo(message.chat.id, photo='https://tourism.rostov-gorod.ru/upload/resize_cache/iblock/ae3/600_400_1/ae3691acbe4efee0b35ecc970fcb4be9.jpg')
        bot.send_message(message.chat.id, s_fun6())

        bot.send_location(message.from_user.id,  47.2110980, 39.6672640)

        bot.send_message(message.chat.id, '.........................................................................')

    if (message.text == 'Кинотеатры'):
        bot.send_message(message.chat.id, 'Начинаю поиск...')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        p1 = types.KeyboardButton('КИНОМАКС-ПЛАЗА')
        p2 = types.KeyboardButton('ДОМ КИНО')
        p3 = types.KeyboardButton('ЧАРЛИ ВАВИЛОН')
        p4 = types.KeyboardButton('КИНОЦЕНТР "БОЛЬШОЙ"')
        p5 = types.KeyboardButton('ГОРИЗОНТ CINEMA&EMOTION')
        p6 = types.KeyboardButton('КИНОМАКС IMAX')
        p7 = types.KeyboardButton('Меню')
        markup.add(p1, p2, p3, p4, p5, p6, p7)
        bot.send_message(message.chat.id, "Куда хочешь пойти?", reply_markup=markup)
    elif(message.text=='КИНОМАКС-ПЛАЗА'):
        bot.send_message(message.chat.id, '.........................................................................')

        def k_fun1():
            url = 'https://tourism.rostov-gorod.ru/attractions/236/5211/'
            response = requests.get(url)
            strar = ''
            soup = BeautifulSoup(response.text, 'lxml')
            quotes = soup.find_all('div', class_='textblock')
            for i in range(0, len(quotes)):
                strar += quotes[i].text
            return strar

        bot.send_message(message.chat.id, 'КИНОМАКС-ПЛАЗА')
        bot.send_photo(message.chat.id, photo='https://tourism.rostov-gorod.ru/upload/resize_cache/iblock/eff/600_400_1/effc296d54006c35939678789575a0a5.jpg')
        bot.send_message(message.chat.id, k_fun1())

        bot.send_location(message.from_user.id, 47.2085040, 39.6310300)

        bot.send_message(message.chat.id, '.........................................................................')

    elif (message.text == 'ДОМ КИНО'):
        bot.send_message(message.chat.id, '.........................................................................')

        def k_fun2():
            url = 'https://tourism.rostov-gorod.ru/attractions/236/5213/'
            response = requests.get(url)
            strar = ''
            soup = BeautifulSoup(response.text, 'lxml')
            quotes = soup.find_all('div', class_='textblock')
            for i in range(0, len(quotes)):
                strar += quotes[i].text
            return strar

        bot.send_message(message.chat.id, 'ДОМ КИНО')
        bot.send_photo(message.chat.id, photo='https://tourism.rostov-gorod.ru/upload/resize_cache/iblock/d9e/600_400_1/d9e2b4d7353f68939e336aaf51190ec3.jpeg')
        bot.send_message(message.chat.id, k_fun2())

        bot.send_location(message.from_user.id,  47.2299400, 39.7359380)

        bot.send_message(message.chat.id, '.........................................................................')

    elif (message.text == 'ЧАРЛИ ВАВИЛОН'):
        bot.send_message(message.chat.id, '.........................................................................')

        def k_fun2():
            url = 'https://tourism.rostov-gorod.ru/attractions/236/5216/'
            response = requests.get(url)
            strar = ''
            soup = BeautifulSoup(response.text, 'lxml')
            quotes = soup.find_all('div', class_='textblock')
            for i in range(0, len(quotes)):
                strar += quotes[i].text
            return strar

        bot.send_message(message.chat.id, 'ЧАРЛИ ВАВИЛОН')
        bot.send_photo(message.chat.id,photo='https://tourism.rostov-gorod.ru/upload/resize_cache/iblock/494/600_400_1/494b1e98bbc65d156be50411c3362e6d.jpg')
        bot.send_message(message.chat.id, k_fun2())

        bot.send_location(message.from_user.id, 47.2810380, 39.7181940)

        bot.send_message(message.chat.id, '.........................................................................')

    elif (message.text == 'КИНОЦЕНТР "БОЛЬШОЙ"'):
        bot.send_message(message.chat.id, '.........................................................................')

        def k_fun3():
            url = 'https://tourism.rostov-gorod.ru/attractions/236/9404/'
            response = requests.get(url)
            strar = ''
            soup = BeautifulSoup(response.text, 'lxml')
            quotes = soup.find_all('div', class_='textblock')
            for i in range(0, len(quotes)):
                strar += quotes[i].text
            return strar

        bot.send_message(message.chat.id, 'КИНОЦЕНТР "БОЛЬШОЙ"')
        bot.send_photo(message.chat.id, photo='https://tourism.rostov-gorod.ru/upload/resize_cache/iblock/873/600_400_1/873427c01ea43f7e1e5dfbc23d967883.jpg')
        bot.send_message(message.chat.id, k_fun3())

        bot.send_location(message.from_user.id, 47.2316770, 39.7262160)

        bot.send_message(message.chat.id, '.........................................................................')


    elif (message.text == 'ГОРИЗОНТ CINEMA&EMOTION'):
        bot.send_message(message.chat.id, '.........................................................................')

        def k_fun4():
            url = 'https://tourism.rostov-gorod.ru/attractions/236/9672/'
            response = requests.get(url)
            strar = ''
            soup = BeautifulSoup(response.text, 'lxml')
            quotes = soup.find_all('div', class_='textblock')
            for i in range(0, len(quotes)):
                strar += quotes[i].text
            return strar

        bot.send_message(message.chat.id, 'ГОРИЗОНТ CINEMA&EMOTION')
        bot.send_photo(message.chat.id, photo='https://tourism.rostov-gorod.ru/upload/iblock/765/7656c6c6eef0ff8458650bd13132c817.png')
        bot.send_message(message.chat.id, k_fun4())

        bot.send_location(message.from_user.id,  47.2609450, 39.7189200)

        bot.send_message(message.chat.id, '.........................................................................')

    elif (message.text == 'КИНОМАКС IMAX'):
        bot.send_message(message.chat.id, '.........................................................................')

        def k_fun5():
            url = 'https://tourism.rostov-gorod.ru/attractions/236/10193/'
            response = requests.get(url)
            strar = ''
            soup = BeautifulSoup(response.text, 'lxml')
            quotes = soup.find_all('div', class_='textblock')
            for i in range(0, len(quotes)):
                strar += quotes[i].text
            return strar

        bot.send_message(message.chat.id, 'КИНОМАКС IMAX')
        bot.send_photo(message.chat.id, photo='https://tourism.rostov-gorod.ru/upload/resize_cache/iblock/b4c/600_400_1/b4c57a330edcc75667fbc03a985a97c0.png')
        bot.send_message(message.chat.id, k_fun5())

        bot.send_location(message.from_user.id,  47.2609450, 39.7189200)

        bot.send_message(message.chat.id, '.........................................................................')

    elif (message.text == 'Торговые центры'):
        bot.send_message(message.chat.id, 'Начинаю поиск...')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        p1 = types.KeyboardButton('ТОРГОВЫЙ ЦЕНТР МОДЫ "А СТОР ПЛАЗА"')
        p2 = types.KeyboardButton('ТРЦ "ЗОЛОТОЙ ВАВИЛОН"')
        p3 = types.KeyboardButton('МЕГАЦЕНТР "ГОРИЗОНТ"')
        p4 = types.KeyboardButton('ТОРГОВО-РАЗВЛЕКАТЕЛЬНЫЙ ЦЕНТР "МЕГА"')
        p5 = types.KeyboardButton('ЦЕНТРАЛЬНЫЙ УНИВЕРМАГ РОСТОВА (ЦУМ)')
        p6 = types.KeyboardButton('ТРЦ "ВАВИЛОН"')
        p7 = types.KeyboardButton('Меню')
        markup.add(p1, p2, p3, p4, p5, p6, p7)
        bot.send_message(message.chat.id, "Куда хочешь пойти?", reply_markup=markup)


    elif(message.text == 'ТОРГОВЫЙ ЦЕНТР МОДЫ "А СТОР ПЛАЗА"'):
        bot.send_message(message.chat.id, '.........................................................................')

        def shop_fun1():
            url = 'https://tourism.rostov-gorod.ru/attractions/413/11588/'
            response = requests.get(url)
            strar = ''
            soup = BeautifulSoup(response.text, 'lxml')
            quotes = soup.find_all('div', class_='textblock')
            for i in range(0, len(quotes)):
                strar += quotes[i].text
            return strar

        bot.send_message(message.chat.id, 'ТОРГОВЫЙ ЦЕНТР МОДЫ "А СТОР ПЛАЗА"')
        bot.send_photo(message.chat.id,photo='https://tourism.rostov-gorod.ru/upload/resize_cache/iblock/38f/600_400_1/38fc5bb3fd0ea9177d0d34d8d7057500.jpg')
        bot.send_message(message.chat.id, shop_fun1())

        bot.send_location(message.from_user.id, 47.224936,39.704673)

        bot.send_message(message.chat.id, '.........................................................................')

    elif (message.text == 'ТРЦ "ЗОЛОТОЙ ВАВИЛОН"'):
        bot.send_message(message.chat.id, '.........................................................................')

        def shop_fun2():
            url = 'https://tourism.rostov-gorod.ru/attractions/413/11583/'
            response = requests.get(url)
            strar = ''
            soup = BeautifulSoup(response.text, 'lxml')
            quotes = soup.find_all('div', class_='textblock')
            for i in range(0, len(quotes)):
                strar += quotes[i].text
            return strar

        bot.send_message(message.chat.id, 'ТРЦ "ЗОЛОТОЙ ВАВИЛОН"')
        bot.send_photo(message.chat.id,
                       photo='https://tourism.rostov-gorod.ru/upload/iblock/ece/ece483de06e4b2d03e127a2973256f92.jpg')
        bot.send_message(message.chat.id, shop_fun2())

        bot.send_location(message.from_user.id, 47.230511,39.610682)

        bot.send_message(message.chat.id, '.........................................................................')

    elif (message.text == 'МЕГАЦЕНТР "ГОРИЗОНТ"'):
        bot.send_message(message.chat.id, '.........................................................................')

        def shop_fun3():
            url = 'https://tourism.rostov-gorod.ru/attractions/413/11166/'
            response = requests.get(url)
            strar = ''
            soup = BeautifulSoup(response.text, 'lxml')
            quotes = soup.find_all('div', class_='textblock')
            for i in range(0, len(quotes)):
                strar += quotes[i].text
            return strar

        bot.send_message(message.chat.id, 'МЕГАЦЕНТР "ГОРИЗОНТ"')
        bot.send_photo(message.chat.id,
                       photo='https://tourism.rostov-gorod.ru/upload/resize_cache/iblock/ab2/600_400_1/ab21594d3e301d2a0cfe82ffae03db76.jpg')
        bot.send_message(message.chat.id, shop_fun3())

        bot.send_location(message.from_user.id, 47.259256,39.718588)

        bot.send_message(message.chat.id, '.........................................................................')


    elif (message.text == 'ТОРГОВО-РАЗВЛЕКАТЕЛЬНЫЙ ЦЕНТР "МЕГА"'):
        bot.send_message(message.chat.id, '.........................................................................')

        def shop_fun4():
            url = 'https://tourism.rostov-gorod.ru/attractions/413/11167/'
            response = requests.get(url)
            strar = ''
            soup = BeautifulSoup(response.text, 'lxml')
            quotes = soup.find_all('div', class_='textblock')
            for i in range(0, len(quotes)):
                strar += quotes[i].text
            return strar

        bot.send_message(message.chat.id, 'ТОРГОВО-РАЗВЛЕКАТЕЛЬНЫЙ ЦЕНТР "МЕГА"')
        bot.send_photo(message.chat.id,
                       photo='https://tourism.rostov-gorod.ru/upload/resize_cache/iblock/04c/600_400_1/04c9dec87a9c5279d31cf7972bd2bd43.jpg')
        bot.send_message(message.chat.id, shop_fun4())

        bot.send_location(message.from_user.id, 47.290057,39.846535)

        bot.send_message(message.chat.id, '.........................................................................')

    elif (message.text == 'ЦЕНТРАЛЬНЫЙ УНИВЕРМАГ РОСТОВА (ЦУМ)'):
        bot.send_message(message.chat.id, '.........................................................................')

        def shop_fun5():
            url = 'https://tourism.rostov-gorod.ru/attractions/413/11586/'
            response = requests.get(url)
            strar = ''
            soup = BeautifulSoup(response.text, 'lxml')
            quotes = soup.find_all('div', class_='textblock')
            for i in range(0, len(quotes)):
                strar += quotes[i].text
            return strar

        bot.send_message(message.chat.id, 'ЦЕНТРАЛЬНЫЙ УНИВЕРМАГ РОСТОВА (ЦУМ)')
        bot.send_photo(message.chat.id,
                       photo='https://tourism.rostov-gorod.ru/upload/resize_cache/iblock/090/600_400_1/0903bfe5a4149aa5a69d9c8728a8972a.jpg')
        bot.send_message(message.chat.id, shop_fun5())

        bot.send_location(message.from_user.id, 47.219967,39.708302)

        bot.send_message(message.chat.id, '.........................................................................')

    elif (message.text == 'ТРЦ "ВАВИЛОН"'):
        bot.send_message(message.chat.id, '.........................................................................')

        def shop_fun6():
            url = 'https://tourism.rostov-gorod.ru/attractions/413/11587/'
            response = requests.get(url)
            strar = ''
            soup = BeautifulSoup(response.text, 'lxml')
            quotes = soup.find_all('div', class_='textblock')
            for i in range(0, len(quotes)):
                strar += quotes[i].text
            return strar

        bot.send_message(message.chat.id, 'ТРЦ "ВАВИЛОН"')
        bot.send_photo(message.chat.id,
                       photo='https://tourism.rostov-gorod.ru/upload/resize_cache/iblock/86e/600_400_1/86e0d72e5708d0266963d9697cad96c3.jpg')
        bot.send_message(message.chat.id, shop_fun6())

        bot.send_location(message.from_user.id, 47.281219,39.717555)

        bot.send_message(message.chat.id, '.........................................................................')

    elif (message.text == 'ЦИРК, ДЕЛЬФИНАРИЙ, ЗООПАРК'):
        bot.send_message(message.chat.id, 'Начинаю поиск...')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        p1 = types.KeyboardButton('МУНИЦИПАЛЬНОЕ БЮДЖЕТНОЕ УЧРЕЖДЕНИЕ РОСТОВСКИЙ-НА-ДОНУ ЗООПАРК')
        p2 = types.KeyboardButton('ДЕЛЬФИНАРИЙ')
        p3 = types.KeyboardButton('РОСТОВСКИЙ ЦИРК')
        p4 = types.KeyboardButton('ТРОГАТЕЛЬНЫЙ ЗООПАРК')
        p5 = types.KeyboardButton('КОЛЕСО ОБОЗРЕНИЯ "ОДНО НЕБО"')
        p6 = types.KeyboardButton('Меню')
        markup.add(p1, p2, p3, p4, p5, p6)
        bot.send_message(message.chat.id, "Куда хочешь пойти?", reply_markup=markup)

    elif (message.text == 'МУНИЦИПАЛЬНОЕ БЮДЖЕТНОЕ УЧРЕЖДЕНИЕ РОСТОВСКИЙ-НА-ДОНУ ЗООПАРК'):
        bot.send_message(message.chat.id, '.........................................................................')

        def zp_fun1():
            url = 'https://tourism.rostov-gorod.ru/attractions/247/5197/'
            response = requests.get(url)
            strar = ''
            soup = BeautifulSoup(response.text, 'lxml')
            quotes = soup.find_all('div', class_='textblock')
            for i in range(0, len(quotes)):
                strar += quotes[i].text
            return strar

        bot.send_message(message.chat.id, 'МУНИЦИПАЛЬНОЕ БЮДЖЕТНОЕ УЧРЕЖДЕНИЕ РОСТОВСКИЙ-НА-ДОНУ ЗООПАРК')
        bot.send_photo(message.chat.id,
                       photo='https://tourism.rostov-gorod.ru/upload/iblock/8ed/8ed34590355ddd3b98c67d84c9d5f48a.jpg')
        bot.send_message(message.chat.id, zp_fun1())

        bot.send_location(message.from_user.id, 47.247025, 39.667199)

        bot.send_message(message.chat.id, '.........................................................................')

    elif (message.text == 'ДЕЛЬФИНАРИЙ'):
        bot.send_message(message.chat.id, '.........................................................................')

        def zp_fun2():
            url = 'https://tourism.rostov-gorod.ru/attractions/247/5198/'
            response = requests.get(url)
            strar = ''
            soup = BeautifulSoup(response.text, 'lxml')
            quotes = soup.find_all('div', class_='textblock')
            for i in range(0, len(quotes)):
                strar += quotes[i].text
            return strar

        bot.send_message(message.chat.id, 'ДЕЛЬФИНАРИЙ')
        bot.send_photo(message.chat.id,
                       photo='https://tourism.rostov-gorod.ru/upload/resize_cache/iblock/5f6/600_400_1/5f6699e442c71aaa27ccc62dfd3e7b23.jpg')
        bot.send_message(message.chat.id, zp_fun2())

        bot.send_location(message.from_user.id, 47.208778,39.627589)

        bot.send_message(message.chat.id, '.........................................................................')

    elif (message.text == 'РОСТОВСКИЙ ЦИРК'):
        bot.send_message(message.chat.id, '.........................................................................')

        def zp_fun3():
            url = 'https://tourism.rostov-gorod.ru/attractions/247/5199/'
            response = requests.get(url)
            strar = ''
            soup = BeautifulSoup(response.text, 'lxml')
            quotes = soup.find_all('div', class_='textblock')
            for i in range(0, len(quotes)):
                strar += quotes[i].text
            return strar

        bot.send_message(message.chat.id, 'РОСТОВСКИЙ ЦИРК')
        bot.send_photo(message.chat.id,
                       photo='https://tourism.rostov-gorod.ru/upload/resize_cache/iblock/120/600_400_1/1204c37ffb7728ba5126d915e24187ba.jpg')
        bot.send_message(message.chat.id, zp_fun3())

        bot.send_location(message.from_user.id, 47.22441,39.705041)

        bot.send_message(message.chat.id, '.........................................................................')

    elif (message.text == 'ТРОГАТЕЛЬНЫЙ ЗООПАРК'):
        bot.send_message(message.chat.id, '.........................................................................')

        def zp_fun4():
            url = 'https://tourism.rostov-gorod.ru/attractions/247/5199/'
            response = requests.get(url)
            strar = ''
            soup = BeautifulSoup(response.text, 'lxml')
            quotes = soup.find_all('div', class_='textblock')
            for i in range(0, len(quotes)):
                strar += quotes[i].text
            return strar

        bot.send_message(message.chat.id, 'ТРОГАТЕЛЬНЫЙ ЗООПАРК')
        bot.send_photo(message.chat.id,
                       photo='https://tourism.rostov-gorod.ru/upload/resize_cache/iblock/37e/600_400_1/37ed5d7aa419d49f5c32ef19534d1ad4.jpg')
        bot.send_message(message.chat.id, zp_fun4())

        bot.send_location(message.from_user.id, 47.229721,39.742618)

        bot.send_message(message.chat.id, '.........................................................................')

    elif (message.text == 'КОЛЕСО ОБОЗРЕНИЯ "ОДНО НЕБО"'):
        bot.send_message(message.chat.id, '.........................................................................')

        def zp_fun5():
            url = 'https://tourism.rostov-gorod.ru/attractions/247/9219/'
            response = requests.get(url)
            strar = ''
            soup = BeautifulSoup(response.text, 'lxml')
            quotes = soup.find_all('div', class_='textblock')
            for i in range(0, len(quotes)):
                strar += quotes[i].text
            return strar

        bot.send_message(message.chat.id, 'КОЛЕСО ОБОЗРЕНИЯ "ОДНО НЕБО"')
        bot.send_photo(message.chat.id,
                       photo='https://tourism.rostov-gorod.ru/upload/resize_cache/iblock/b44/600_400_1/b44233e4a43c0646b89b2d03f64ecd20.jpg')
        bot.send_message(message.chat.id, zp_fun5())

        bot.send_location(message.from_user.id, 47.229721,39.742618)

        bot.send_message(message.chat.id, '.........................................................................')









# Для стабильной работы бота ###################

while(1):
    bot.polling(none_stop=True)

###############################################