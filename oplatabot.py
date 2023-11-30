import telebot
from telebot import types
from config import token

bot=telebot.TeleBot(token)

# Создаем клавиатуры для интерфейса бота
keyboard1 = types.ReplyKeyboardMarkup(True, True)
item1 = types.KeyboardButton('Новости')
item2 = types.KeyboardButton('Оплата')
item3 = types.KeyboardButton('Подключиться')
keyboard1.add(item1, item2)
keyboard1.add(item3)

# Реакция на команду start
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,"Привет, бот поможет тебе оплатить связь выбери нужный вариант в меню", reply_markup=keyboard1)

# Реакции на отправляемые команды
@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == 'Новости':
        bot.send_message(message.chat.id, 'В этом разделе будут отображаться последние новости связанные с связью', reply_markup=keyboard1)
    elif message.text == 'Оплата':
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Оплата", url="https://www.youtube.com/shorts/yWntt_agA2s")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Привет! Для оплаты нажми на кнопку", reply_markup=keyboard)
    elif message.text == 'Подключиться':
        bot.send_message(message.chat.id, 'Это возможность подключиться: отправь свой телеграм и кто ты', reply_markup=keyboard1)
    elif message.text.isalpha():
        bot.send_message(message.chat.id, 'Твое сообщение отправлено на проверку', reply_markup=keyboard1)
        bot.send_message('107233142', message.text)
    

# Постоянная работа бота
while True:
    try:
        bot.polling(none_stop=True, timeout=90)
    except Exception as e:
        print(datetime.datetime.now(), e)
        time.sleep(5)
        continue
