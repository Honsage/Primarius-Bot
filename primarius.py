from dotenv import dotenv_values
from telebot import TeleBot


config = dotenv_values()
bot = TeleBot(token=config['API_TOKEN'])


@bot.message_handler(commands=['start'])
def handle_start_command(message):
    chat_id = message.chat.id
    name = message.chat.first_name
    bot.send_message(
        chat_id=chat_id,
        text=f'Здравствуйте, {name}, я бот Primarius.'
    )

@bot.message_handler(content_types=['text'])
def handle_text(message):
    print(message)
    chat_id = message.chat.id
    bot.send_message(
        chat_id=chat_id,
        text='Пока что я не понимаю сообщения :('
    )


bot.polling()
