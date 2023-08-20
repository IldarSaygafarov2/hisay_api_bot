from tg_bot.data.loader import bot
from telebot import types


@bot.message_handler(commands=['start'])
def command_start(message: types.Message):
    chat_id = message.chat.id
    first_name = message.from_user.first_name

    bot.send_message(chat_id, f"Hello, {first_name}")
