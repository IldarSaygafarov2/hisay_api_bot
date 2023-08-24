from telebot import types

from tg_bot.data.loader import bot
from tg_bot.keyboards.reply import start_menu


@bot.message_handler(commands=['start'])
def command_start(message: types.Message):
    chat_id = message.chat.id
    first_name = message.from_user.first_name

    bot.send_message(chat_id, f"Приветствую тебя, {first_name}. Чтобы начать использовать бот, пройди регистрацию",
                     reply_markup=start_menu())


