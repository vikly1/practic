import random
import telebot
from telebot import types

bot = telebot.TeleBot('6287669618:AAH45VJ1VUhbBfWkj_mlARKvGEbzJGBhGmo')


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "", parse_mode='html')


@bot.message_handler(content_types=['photo'])
def u_photo(message):
    bot.send_message(message.chat.id, 'Какая классная картинка!')


@bot.message_handler(content_types=['video'])
def u_video(message):
    bot.send_message(message.chat.id, 'Какое классное видео!')


@bot.message_handler()
def get_user_text(message):
    if message.text == "hello" or message.text == "Hello" or message.text == "привет" or message.text == "Привет" or message.text == "здравствуй" or message.text == "Здравствуй":
        bot.send_message(message.chat.id, "приветики", parse_mode='html')
    elif message.text == "как дела":
        bot.send_message(message.chat.id, "не знаю, я, в принципе, всего лишь робот, который всегда будет чувствовать себя, допустим, нормально. Надеюсь, тебя устроит мой ответ", parse_mode='html')
    elif message.text == "чем занимаешься?" or message.text == "что делаешь?":
        bot.send_message(message.chat.id, "радуюсь каждой минуте своего сущестования, а так же общаюсь с тобой", parse_mode='html')
    elif message.text == "скинь котика":
        photo =  open('cat.jpeg', 'rb')
        bot.send_photo(message.chat.id, photo)
    elif message.text == "что ты умеешь" or message.text == "что ты еще умеешь":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("выдать рандомное фото", callback_data='img_path'))
        markup.add(types.InlineKeyboardButton("сгенерировать случайное число", callback_data='test'))
        bot.send_message(message.chat.id, 'Вот что я умею', reply_markup=markup)
    else:
        bot.send_message(message.chat.id, "Не понимаю тебя, можешь написать ЧТО ТЫ УМЕЕШЬ для выбора операций", parse_mode='html')



@bot.callback_query_handler(func=lambda c: c.data == "test")
def rand(c):

    a = random.randint(0,100000000)
    bot.edit_message_text(text=str(a),chat_id=c.from_user.id,message_id=c.message.id)


@bot.callback_query_handler(func=lambda d: d.data =='img_path')
def choose(d):
    img_list = ['cats/cat.jpeg', 'cats/cat2.jpg', 'cats/cat3.jpg','cats/moon.jpg','cats/sun.jpg']
    img_chsoe = random.choice(img_list)
    bot.send_photo(photo=open(img_chsoe, 'rb'), chat_id=d.from_user.id)


bot.polling(none_stop=True)