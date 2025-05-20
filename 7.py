import telebot
import random
import time
import threading
from telebot import types

# Создаем экземпляр бота с токеном
TOKEN = '8187173269:AAEQ8cYFTeBCKVho5XNRcJ5gGVXXe50AVcc'
bot = telebot.TeleBot(TOKEN)


# Функция для отправки уведомления о завершении таймера
def notify_timer(chat_id, duration):
    time.sleep(duration)
    bot.send_message(chat_id, f"{duration} истекло")


@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_dice = types.KeyboardButton("/dice")
    button_timer = types.KeyboardButton("/timer")
    keyboard.add(button_dice, button_timer)

    bot.send_message(message.chat.id, "Привет! Выберите действие:", reply_markup=keyboard)


@bot.message_handler(commands=['dice'])
def dice_menu(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_one_die = types.KeyboardButton("Кинуть 1 шестигранный кубик")
    button_two_dice = types.KeyboardButton("Кинуть 2 шестигранных кубика")
    button_twenty_sided = types.KeyboardButton("Кинуть 20-гранный кубик")
    button_back = types.KeyboardButton("Вернуться назад")
    keyboard.add(button_one_die, button_two_dice, button_twenty_sided, button_back)

    bot.send_message(message.chat.id, "Выберите вариант броска кубиков:", reply_markup=keyboard)


@bot.message_handler(func=lambda message: message.text == "Кинуть 1 шестигранный кубик")
def roll_one_die(message):
    result = random.randint(1, 6)
    bot.reply_to(message, f"Вы бросили кубик и получили: {result}")


@bot.message_handler(func=lambda message: message.text == "Кинуть 2 шестигранных кубика")
def roll_two_dice(message):
    result1 = random.randint(1, 6)
    result2 = random.randint(1, 6)
    bot.reply_to(message, f"Вы бросили два кубика и получили: {result1} и {result2}")


@bot.message_handler(func=lambda message: message.text == "Кинуть 20-гранный кубик")
def roll_twenty_sided(message):
    result = random.randint(1, 20)
    bot.reply_to(message, f"Вы бросили 20-гранный кубик и получили: {result}")


@bot.message_handler(func=lambda message: message.text == "Вернуться назад")
def back_to_start(message):
    start(message)


@bot.message_handler(commands=['timer'])
def timer_menu(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_30s = types.KeyboardButton("30 секунд")
    button_1m = types.KeyboardButton("1 минута")
    button_5m = types.KeyboardButton("5 минут")
    button_back = types.KeyboardButton("Вернуться назад")
    keyboard.add(button_30s, button_1m, button_5m, button_back)

    bot.send_message(message.chat.id, "Выберите время для таймера:", reply_markup=keyboard)


@bot.message_handler(func=lambda message: message.text == "30 секунд")
def timer_30s(message):
    bot.reply_to(message, "Засекаю 30 секунд...")
    threading.Thread(target=notify_timer, args=(message.chat.id, 30)).start()


@bot.message_handler(func=lambda message: message.text == "1 минута")
def timer_1m(message):
    bot.reply_to(message, "Засекаю 1 минуту...")
    threading.Thread(target=notify_timer, args=(message.chat.id, 60)).start()


@bot.message_handler(func=lambda message: message.text == "5 минут")
def timer_5m(message):
    bot.reply_to(message, "Засекаю 5 минут...")
    threading.Thread(target=notify_timer, args=(message.chat.id, 300)).start()


@bot.message_handler(func=lambda message: message.text == "Вернуться назад")
def back_to_start_from_timer(message):
    start(message)


# Запускаем бота
if __name__ == '__main__':
    print("Бот запущен...")
    bot.polling(none_stop=True)

# t.me/cube_yullkk_bot
