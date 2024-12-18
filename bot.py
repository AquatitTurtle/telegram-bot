import telebot
import time
from secrets import secrets
from telebot import types

token = secrets.get('BOT_API_TOKEN')
bot = telebot.TeleBot(token)

# Увеличьте timeout для API-запросов
telebot.apihelper.TIMEOUT = 60  # Увеличение до 60 секунд
telebot.apihelper.READ_TIMEOUT = 60

"""ReplyKeyboardMarkup"""
# kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
# btn1 = types.KeyboardButton(text='Кнопка 1')
# btn2 = types.KeyboardButton(text='Кнопка 2')
# kb.add(btn1, btn2)

"""InlineKeyboardMarkup + URL"""
# kb = types.InlineKeyboardMarkup(row_width=1)
# btn1 = types.InlineKeyboardButton(text='Instagram', url='https://www.instagram.com/harmonyhub.perfume/')
# btn2 = types.InlineKeyboardButton(text='YouTube', url='https://www.youtube.com/')
# kb.add(btn1, btn2)

"""InlineKeyboardMarkup + Switch buttons"""
# переадрессация с бота на ЛС в ТГ
# markup = types.InlineKeyboardMarkup()
# switch = types.InlineKeyboardButton(text='Кнопка 1', url='https://t.me/crafty_sausage')
# markup.add(switch)

# /start команда

@bot.message_handler(commands=['start', 'menu'])
def start_message(message):
    bot_message = """
Привет, мы рады, что ты с нами!

Этот бот поможет выбрать аромат, который станет твоей второй кожей.
    
Давай начнём!
"""
    # Проверка на пустой текст
    if not bot_message.strip():
        bot_message = "Привет! Давай начнём!"

    # Создаём InlineKeyboardMarkup
    kb = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton(text='🌌 Подбор по натальной карте', callback_data='map') #сделать перессылку сразу на Хабу
    btn2 = types.InlineKeyboardButton(text='📦 Готовые сеты', callback_data='sets')
    btn3 = types.InlineKeyboardButton(text='1️⃣ Хочу один аромат', callback_data='single')
    btn4 = types.InlineKeyboardButton(text='📄 Каталог', callback_data='catalog')

    kb.add(btn1, btn2, btn3, btn4)

    photo_url = r'https://i.pinimg.com/736x/b3/db/cc/b3dbccd98fd10ced1ea746010ba216ae.jpg'
    bot.send_photo(message.chat.id, photo_url,caption=bot_message, reply_markup=kb)




@bot.callback_query_handler(func=lambda callback: callback.data)
def check_callback_data_main_menu(callback):
    try:
        response_text = None  # Устанавливаем значение по умолчанию

        if callback.data == 'map':
            response_text = show_map(callback.message)
        elif callback.data == 'sets':
            response_text = show_sets(callback.message)
        elif callback.data == 'single':
            response_text = single(callback.message)
        elif callback.data == 'catalog':
            response_text = "Огранизуем подарок вашему фавориту!"
        elif callback.data == 'setForTest':
            response_text = show_setForTest(callback.message)
        elif callback.data == 'setOfTwelve':
            response_text = show_setOfTwelve(callback.message)
        elif callback.data == 'setForProfessional':
            response_text = show_setForProfessional(callback.message)
        elif callback.data == 'setForFan':
            response_text = show_setForFan(callback.message)
        elif callback.data == 'setForLegend':
            response_text = show_setForLegend(callback.message)
        elif callback.data == 'setForMan':
            response_text = show_male_set(callback.message)
        elif callback.data == 'setForLady':
            response_text = show_female_set(callback.message)
        elif callback.data == 'setForLovers':
            response_text = show_lovers_set(callback.message)
        elif callback.data == 'back':
            response_text = back_menu(callback.message)
        elif callback.data == 'back_sets':
            response_text = back_sets(callback.message)
        else:
            response_text = None  # На случай неизвестных callback

        # Отправляем сообщение, только если есть корректный текст
        if response_text and response_text.strip():
            # bot.send_message(callback.message.chat.id, response_text)
            print("Все работает успешно")
        else:
            print("Callback вернул пустое сообщение.")  # Логируем ситуацию вместо отправки текста
    except Exception as e:
        print(f"Ошибка при обработке callback: {e}")



@bot.message_handler(commands=['map'])
def show_map(message):
    text = """
    Хочешь узнать, каким может быть парфюм подобраный специально для тебя?

Мы соединяем искусство парфюмерии с глубокой индивидуальностью натальной карты, чтобы подобрать аромат, который раскроет историю твоей души.

Наша уникальная программа ароматов станет для тебя второй кожей, раскрытием феромонов твоего тела и даже личным психологом, который может поднять настроение, уверенность в себе, активировать ресурсы, раскрыть грани себя настоящего и прийти к внутренней гармонии.

Нужны только твоя дата, время и место рождения. Нажми кнопку и получи свой особенный ароматный опыт, который создан для твоей души. 👇
    """
    kb = types.InlineKeyboardMarkup(row_width=1)
    iKnowBtn = types.InlineKeyboardButton(text='Я знаю все данные', url='https://t.me/HaarmonyHub')
    IDontKnowBtn = types.InlineKeyboardButton(text='Я не знаю всех данных ', url='https://t.me/HaarmonyHub')
    back_btn = types.InlineKeyboardButton(text='🔙 Назад', callback_data='back')
    kb.add(iKnowBtn, IDontKnowBtn, back_btn)

    photo_url = r'https://i.pinimg.com/736x/f6/ca/2a/f6ca2ac516ab32b11c02481840b22354.jpg'

    bot.send_photo(message.chat.id, photo_url,
                   text, reply_markup=kb)
    return "Вот твоя натальная карта! 🌌"


@bot.message_handler(commands=['sets'])
def show_sets(message):
    text = """
    Мы уже приготовили для тебя сеты!\nТебе только осталось выбрать свое."""
    kb = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton(text='Пробный сет', callback_data='setForTest')
    btn2 = types.InlineKeyboardButton(text='12 Наслаждений', callback_data='setOfTwelve')
    btn3 = types.InlineKeyboardButton(text='Профессионал', callback_data='setForProfessional')
    btn4 = types.InlineKeyboardButton(text='Фанат', callback_data='setForFan')
    btn5 = types.InlineKeyboardButton(text='Легенда', callback_data='setForLegend')
    btn6 = types.InlineKeyboardButton(text='"Seven" for Him', callback_data='setForMan')
    btn7 = types.InlineKeyboardButton(text='"Seven" for Her', callback_data='setForLady')
    btn8 = types.InlineKeyboardButton(text='for Lovers ❤', callback_data='setForLovers')
    back_btn = types.InlineKeyboardButton(text='🔙 Назад', callback_data='back')

    kb.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, back_btn)

    photo_url = r'https://i.pinimg.com/736x/84/1f/fd/841ffda1e862b4304d4b19fde4cfd652.jpg'
    bot.send_photo(message.chat.id, photo_url, text, reply_markup=kb)
    return "Вот твои сеты "


@bot.message_handler(commands=['single'])
def single(message):
    single_message = "Вы хотите выбрать один парфюм.\nВысылаю наш каталог..."
    kb = types.InlineKeyboardMarkup(row_width=1)
    back_btn = types.InlineKeyboardButton(text='🔙 Назад', callback_data='back')
    kb.add(back_btn)

    photo_url = r'https://i.pinimg.com/736x/4c/76/c8/4c76c8a488adfc474698ab9aea9b34b9.jpg'
    bot.send_photo(message.chat.id, photo_url,
                   single_message, reply_markup=kb)

    # отправка каталого 👇
    file = open('HaarmonyHub Каталог.pdf', 'rb')
    bot.send_document(message.chat.id, file)

    time.sleep(2)
    contact_text = """Если хотите узнать больше \nподробностей, Вы сможете \nсвязаться с нашим специалистом."""
    kb2 = types.InlineKeyboardMarkup(row_width=1)
    contact_btn = types.InlineKeyboardButton(text='Связаться 📱', url='https://t.me/HaarmonyHub')
    kb2.add(contact_btn)
    bot.send_message(message.chat.id, contact_text, reply_markup=kb2)

    return "Вот наш каталог"


@bot.message_handler(commands=['catalog'])
def show_catalog(message):
    catalog_text = """Добро пожаловат в меню каталога.
    Сейчас наш бот вышлет вам каталог..."""
    kb = types.InlineKeyboardMarkup(row_width=1)
    back_btn = types.InlineKeyboardButton(text='🔙 Назад', callback_data='back')
    kb.add(back_btn)

    link = r'https://i.pinimg.com/736x/0f/62/f1/0f62f1ab3ec0cf63979ab646cb54ce89.jpg'
    bot.send_photo(message.chat.id, link, catalog_text, reply_markup=kb)

    # отправка каталого 👇
    file = open('HaarmonyHub Каталог.pdf', 'rb')
    bot.send_document(message.chat.id, file)

    time.sleep(2)
    contact_text = """Если хотите узнать больше \nподробностей, Вы сможете \nсвязаться с нашим специалистом."""
    kb2 = types.InlineKeyboardMarkup(row_width=1)
    contact_btn = types.InlineKeyboardButton(text='Связаться 📱', url='https://t.me/HaarmonyHub')
    kb2.add(contact_btn)
    bot.send_message(message.chat.id, contact_text, reply_markup=kb2)

    return "Вот наш каталог"



def show_setForTest(message):
    setForTest_text = """5 ароматов по 3мл"""
    kb = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton(text='Заказать 📦', callback_data='buy')
    btn2 = types.InlineKeyboardButton(text='🔙 Назад', callback_data='back_sets')
    kb.add(btn1, btn2)

    photo_url = r'https://i.pinimg.com/736x/fe/74/9d/fe749dd5d4c50c5fae73c141b46a96f0.jpg'

    bot.send_photo(message.chat.id, photo_url, setForTest_text, reply_markup=kb)
    return "Инфо о сете"

def show_setOfTwelve(message):
    setOfTwelve_text = """12 ароматов на целый год. Один аромат на каждый месяц."""
    kb = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton(text='Заказать 📦', callback_data='buy')
    btn2 = types.InlineKeyboardButton(text='🔙 Назад', callback_data='back_sets')
    kb.add(btn1, btn2)

    photo_url = r'https://i.pinimg.com/736x/c5/d0/59/c5d05902e9d8c2cb35c86cf5bad00db8.jpg'
    bot.send_photo(message.chat.id, photo_url, setOfTwelve_text, reply_markup=kb)
    return "Инфо о сете"

def show_setForProfessional(message):
    setProfessional_text = """4 аромата по 30мл"""
    kb = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton(text='Заказать 📦', callback_data='buy')
    btn2 = types.InlineKeyboardButton(text='🔙 Назад', callback_data='back_sets')
    kb.add(btn1, btn2)

    photo_url = r'https://i.pinimg.com/736x/47/4b/20/474b20670228dadb245238bd3c5c51a7.jpg'
    bot.send_photo(message.chat.id, photo_url,
                   setProfessional_text, reply_markup=kb)
    return "Инфо о сете"

def show_setForFan(message):
    setFan_text = """3 аромата по 50 мл"""
    kb = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton(text='Заказать 📦', callback_data='buy')
    btn2 = types.InlineKeyboardButton(text='🔙 Назад', callback_data='back_sets')
    kb.add(btn1, btn2)

    photo_url = r'https://i.pinimg.com/736x/2c/99/7c/2c997c702342b839d4f98193721a7efa.jpg'
    bot.send_photo(message.chat.id, photo_url, setFan_text, reply_markup=kb)
    return "Инфо о сете"

def show_setForLegend(message):
    setForLegend_text = """3 аромата по 100мл"""
    kb = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton(text='Заказать 📦', callback_data='buy')
    btn2 = types.InlineKeyboardButton(text='🔙 Назад', callback_data='back_sets')
    kb.add(btn1, btn2)

    photo_url = r'https://i.pinimg.com/736x/37/3d/ab/373daba1a74f00ac4ac420af2af780ac.jpg'
    bot.send_photo(message.chat.id, photo_url, setForLegend_text, reply_markup=kb)
    return "Инфо о сете"

def show_male_set(message):
    male_set_text = """Семь ароматов только для него"""
    kb = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton(text='Заказать 📦', callback_data='buy')
    btn2 = types.InlineKeyboardButton(text='🔙 Назад', callback_data='back_sets')
    kb.add(btn1, btn2)

    photo_url = r'https://i.pinimg.com/736x/b7/72/bb/b772bb80f365ff7fa3d2fb038854ec89.jpg'
    bot.send_photo(message.chat.id, photo_url,
                  male_set_text, reply_markup=kb)
    return "Подробности о сете \"Seven\" for Him"

def show_female_set(message):
    female_set_text = """Семь головокружительных ароматов для нее"""
    kb = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton(text='Заказать 📦', callback_data='buy')
    btn2 = types.InlineKeyboardButton(text='🔙 Назад', callback_data='back_sets')
    kb.add(btn1, btn2)

    bot.send_photo(message.chat.id, r'https://i.pinimg.com/736x/55/21/87/552187b01acf20002e8c717385f021ef.jpg',
                   female_set_text, reply_markup=kb)
    return "Подробности о сете \"Seven\" for Her"

def show_lovers_set(message):
    lovers_set_text = """Один особенный набор для двух любящий людей ❤"""
    kb = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton(text='Заказать 📦', callback_data='buy')
    btn2 = types.InlineKeyboardButton(text='🔙 Назад', callback_data='back_sets')
    kb.add(btn1, btn2)

    bot.send_photo(message.chat.id, r'https://i.pinimg.com/736x/64/fd/68/64fd685aafbb0c7140a489f28cf9cd2d.jpg',
                   lovers_set_text, reply_markup=kb)
    return "Подробности о сете for Lovers"

def back_menu(message):
    start_message(message)
    return "Back for menu"

def back_sets(message):
    show_sets(message)
    return "Back for sets"


bot.infinity_polling()
