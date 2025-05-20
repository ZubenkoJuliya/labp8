import telebot
from telebot import types
import datetime

# Создаем экземпляр бота с токеном
TOKEN = '7826333479:AAEzX69FIP9CLZzq6DSc6aiObc64vcPZ2wQ'
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    # Создаем клавиатуру
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_time = types.KeyboardButton("/time")
    button_date = types.KeyboardButton("/date")
    keyboard.add(button_time, button_date)

    # Отправляем приветственное сообщение с кнопками
    bot.send_message(message.chat.id, "Привет! Нажми на кнопку, чтобы узнать текущее время или дату:",
                     reply_markup=keyboard)


@bot.message_handler(commands=['time'])
def send_time(message):
    current_time = datetime.datetime.now().strftime('%H:%M:%S')  # Получаем текущее время
    response = f'Текущее время: {current_time}'
    bot.reply_to(message, response)


@bot.message_handler(commands=['date'])
def send_date(message):
    current_date = datetime.datetime.now().strftime('%Y-%m-%d')  # Получаем текущую дату
    response = f'Текущая дата: {current_date}'
    bot.reply_to(message, response)


# Запускаем бота
if __name__ == '__main__':
    print("Бот запущен...")
    bot.polling(none_stop=True)

# t.me/time_date_yullkk_bot
