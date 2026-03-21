from dotenv import dotenv_values
from telebot import TeleBot


config = dotenv_values()
bot = TeleBot(token=config['API_TOKEN'])


@bot.message_handler(content_types=['text'])
def handle_text(message):
    chat_id = message.chat.id
    bot.send_message(chat_id=chat_id, text='Привет, я бот Primarius.')


bot.polling()
