from bot import bot # Импортируем объект бота
from messages import * # Инмпортируем все с файла сообщений


@bot.message_handler(commands=['start'])
# Выполняется, когда пользователь нажимает на start
def send_welcome(message):
    bot.send_message(message.chat.id, HELLO_MESSAGE)

@bot.message_handler(commands=['help'])
# Выполняется, когда пользователь нажимает на start
def send_welcome(message):
    bot.send_message(message.chat.id, HELP_MESSAGE)


@bot.message_handler(content_types=['text'])
def handle_text_messages(message):
    if message.text == 'Привет':
        bot.send_message(message.from_user.id, 'Привет')
    elif message.text == 'Кто ты?':
        bot.send_message(message.from_user.id, 'Я бот')
    elif message.text == 'Как тебя зовут?':
        bot.send_message(message.from_user.id, 'Меня зовут Drunkart')
    elif message.text == 'Что ты умеешь?':
        bot.send_message(message.from_user.id, '"Я умею отвечать на несколько простых вопросов - кто я, как меня зовут и что я умею делать')
    else:
        bot.send_message(message.from_user.id, 'Я тебя не понимаю. Напиши что-то другое.')


if __name__ == '__main__':
     bot.polling(none_stop=True)