from dotenv import dotenv_values
from telebot import TeleBot


config = dotenv_values()
bot = TeleBot(token=config['API_TOKEN'])

chat_id = config['TEST_CHAT']
message = 'Вам телеграмма!'
bot.send_message(chat_id, message)
