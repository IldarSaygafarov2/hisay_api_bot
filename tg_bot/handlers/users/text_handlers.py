from telebot import types

from tg_bot.data.loader import bot
from tg_bot.keyboards.reply import phone_number_button


@bot.message_handler(func=lambda msg: msg.text == 'Пользователь')
def register_simple_user(message: types.Message):
    chat_id = message.chat.id

    bot.send_message(chat_id, "Напишите или отправьте ваш номер телефона", reply_markup=phone_number_button())
    bot.register_next_step_handler(message, get_phone_number)


def get_phone_number(message: types.Message):
    chat_id = message.chat.id

    phone_number = ""

    if message.contact:
        phone_number = message.contact.phone_number
    elif message.text:
        phone_number = message.text

    bot.send_message(chat_id, "Напишите ваше ФИО. Пример: 'Иванов Иван Иванович'",
                     reply_markup=types.ReplyKeyboardRemove())
    bot.register_next_step_handler(message, get_fullname, phone_number)


def get_fullname(message: types.Message, phone_number):
    chat_id = message.chat.id
    fullname = message.text

    if not len(fullname.split()) == 3:
        bot.reply_to('Введите ФИО в указанном выше примере')
        return

    bot.send_message(chat_id, "Регистрация прошла ")



@bot.message_handler(func=lambda msg: msg.text == 'Сервис')
def register_service(message: types.Message):
    chat_id = message.chat.id

    bot.send_message(chat_id, "Регистрация для сервиса")
