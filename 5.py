import telebot

# Создаем экземпляр бота с токеном
TOKEN = '7366047453:AAGzEFKH5QsBaJQPhUIVOQnGbggomC-eHec'
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    # Отправляем приветственное сообщение
    bot.reply_to(message, "Привет! Я эхо-бот. Напиши мне что-нибудь!")


@bot.message_handler(func=lambda message: True)
def echo(message):
    # Формируем ответное сообщение
    response = f'Я получил сообщение: {message.text}'
    # Отправляем ответ
    bot.reply_to(message, response)


# Запускаем бота
if __name__ == '__main__':
    print("Бот запущен...")
    bot.polling(none_stop=True)

# t.me/echo_yullkk1_bot
