from telebot import types

from tg_bot.data.loader import bot
from tg_bot.helpers.utils import __get_phone_number
from tg_bot.helpers import api
from tg_bot.keyboards.reply import phone_number_button, start_request_kb
from tg_bot.handlers.users.commands import command_start


@bot.message_handler(func=lambda msg: msg.text == 'Пользователь')
def register_simple_user(message: types.Message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Напишите или отправьте ваш номер телефона", reply_markup=phone_number_button())
    bot.register_next_step_handler(message, get_phone_number)


def get_phone_number(message: types.Message):
    chat_id = message.chat.id
    phone_number = __get_phone_number(message)
    bot.send_message(chat_id,
                     "Напишите ваше ФИО. Пример: 'Иванов Иван Иванович'",
                     reply_markup=types.ReplyKeyboardRemove())
    bot.register_next_step_handler(message, get_fullname, phone_number)


def get_fullname(message: types.Message, phone_number):
    chat_id = message.chat.id
    fullname = message.text

    if not len(fullname.split()) == 3:
        bot.reply_to('Введите ФИО в указанном выше примере')
        return

    user_data = {
        "tg_username": message.from_user.username or phone_number,
        "fullname": fullname,
        "tg_chat_id": chat_id,
        "phone_number": phone_number
    }

    api.create_simple_user(user_data)

    bot.send_message(chat_id, "Регистрация прошла успешно")
    command_start(message)

