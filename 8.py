import telebot
from telebot import types

# Создаем экземпляр бота с токеном
TOKEN = '7568814048:AAEIbZHXObj36ZAT4rKGJas-z9OGOzs8Inw'  # Замените на ваш токен
bot = telebot.TeleBot(TOKEN)

# Залы музея и их описания
halls = {
    1: {
        "name": "Зал 1",
        "description": "В данном зале представлено путешесвие на космическую станцию, расположенную в 600 километрах над Землёй. Посмотрите в иллюминатор и узнайте, как Луна может стать источником возобновляемой энергии для всей планеты.",
        "next": [2],  # Возможные залы для перехода
        "image": "https://motf-p-16570672ab7e.imgix.net/4ff564ad-2a4c-42e7-b3fa-ffb3dae9fd78/Sol_L1FT_and_Hub.png?auto=compress%2Cformat&fit=min&fm=jpg&q=80&rect=703%2C0%2C2461%2C1845"
    },
    2: {
        "name": "Зал 2",
        "description": "В данном зале представлено смешанная реальность, воссоздающую тропические леса Амазонии. Посмотрите, как взаимодействуют сотни видов, и разглядите детали, невидимые невооружённым глазом.",
        "next": [3],
        "image": "https://i.pinimg.com/originals/30/e0/72/30e0720b73b0c0c241c1835ce742516a.jpg"
    },
    3: {
        "name": "Зал 3",
        "description": "В данном зале представлено библиотека ДНК, содержащую информацию о тысячах видов, где вы сможете исследовать, собирать и вносить свой вклад в изучение чудес природы.",
        "next": [1, 4],
        "image": "https://i.pinimg.com/736x/d8/ae/3e/d8ae3e5dc394b089f29e85673b6983af.jpg"
    },
    4: {
        "name": "Зал 4",
        "description": "В данном зале представлено убежище от цифровой жизни. Исследуйте центр человеческих чувств, где вам предложат отключиться от технологий и восстановить связь со своим разумом, телом и духом.",
        "next": [1],
        "image": "https://motf-p-16570672ab7e.imgix.net/eb99a2b1-ac23-4387-8138-1d3940c9cd7c/SandBath_FinalSHOT03_.jpg?auto=compress%2Cformat&fit=min&fm=jpg&q=80&rect=473%2C0%2C1439%2C1080"
    }
}

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def start(message):
    welcome_message = "Добро пожаловать в музей БУДУЩЕГО! Пожалуйста, сдайте верхнюю одежду в гардероб!"
    bot.send_message(message.chat.id, welcome_message)
    show_hall_info(message.chat.id, 1)  # Показать информацию о первом зале

def show_hall_info(chat_id, hall_number):
    hall = halls[hall_number]
    hall_info = f"{hall['description']}\n\nВы можете перейти в следующие залы:\n"
    # Создаем клавиатуру
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for next_hall in hall["next"]:
        button = types.KeyboardButton(f"Перейти в {halls[next_hall]['name']}")
        keyboard.add(button)
    # Добавляем кнопку выхода, если это первый зал
    if hall_number == 1:
        keyboard.add(types.KeyboardButton("Выход"))
    # Отправляем изображение и текст
    bot.send_photo(chat_id, hall["image"], caption=hall_info, reply_markup=keyboard)

# Обработчик всех текстовых сообщений
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    text = message.text
    chat_id = message.chat.id

    if text == "Выход":
        exit_museum(chat_id)
        return

    # Проверяем, есть ли в тексте переход в зал
    for hall_number, hall in halls.items():
        if text == f"Перейти в {hall['name']}":
            show_hall_info(chat_id, hall_number)
            return

    # Если ничего не подошло, отправляем сообщение
    bot.send_message(chat_id, "Пожалуйста, выберите доступную опцию.")

def exit_museum(chat_id):
    goodbye_message = "Всего доброго, не забудьте забрать верхнюю одежду в гардеробе!"
    bot.send_message(chat_id, goodbye_message)

# Запуск бота
if __name__ == '__main__':
    print("Бот запущен...")
    bot.polling(none_stop=True)


#t.me/museum_yullkk_bot

