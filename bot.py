import telebot
from telebot import types
import config
bot = telebot.TeleBot('6721352277:AAFjpmg4cztNhrp7phRw6IdrCL6RdQ_xJR8')
@bot.message_handler(content_types=['text', 'audio', 'document', 'photo'])
def get_text_messages(message):
if message.text == '/start':
bot.send_message(message.from_user.id,'Напиши "Привет"')
elif message.text == 'Привет':
markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
btn1 = types.KeyboardButton("Моя статистика")
btn2 = types.KeyboardButton("Анализ последней игры")
markup.add(btn1, btn2)
bot.send_message(message.chat.id, text="С чего начнем?",reply_markup=markup)
markup = types.InlineKeyboardMarkup()
button1 = types.InlineKeyboardButton("Сайт Stratz", url='https://stratz.com/')
markup.add(button1)
bot.send_message(message.chat.id,"Привет, {0.first_name}! Нажми на кнопку и перейди на сайт)".format(message.from_user),reply_markup=markup)
bot.polling(none_stop=True, interval=0)