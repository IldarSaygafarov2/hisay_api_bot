import os
import time

import requests
from telebot import types

from tg_bot.data import config
from tg_bot.data.loader import bot
from tg_bot.helpers import api
from tg_bot.helpers.utils import __get_phone_number
from tg_bot.keyboards.reply import phone_number_button, services_menu


def __get_file_id(message: types.Message) -> str | None:
    """Получаем id отправленного файла, в зависимости от того, как его отправил пользователь."""
    file_id = None

    if message.photo:
        file_id = message.photo[0].file_id
    elif message.document:
        file_id = message.document.file_id

    return file_id


@bot.message_handler(func=lambda msg: msg.text == 'Сервис')
def register_service(message: types.Message):
    chat_id = message.chat.id

    bot.send_message(chat_id, "Напишите ФИО владельца сервиса. Пример: 'Иванов Иван Иванович'")
    bot.register_next_step_handler(message, get_fullname_process_number)


def get_fullname_process_number(message: types.Message):
    chat_id = message.chat.id
    fullname = message.text

    if not len(fullname.split()) == 3:
        bot.send_message(chat_id, "Вы что-то забыли")
        register_service(message)
        return

    bot.send_message(chat_id, "Отправьте или напишите ваш номер телефона", reply_markup=phone_number_button())
    bot.register_next_step_handler(message, get_number_process_photo, fullname)


def get_number_process_photo(message: types.Message, fullname: str):
    chat_id = message.chat.id
    phone_number = __get_phone_number(message)

    bot.send_message(chat_id, "Отправьте фотографию вашего сертификата", reply_markup=types.ReplyKeyboardRemove())
    bot.register_next_step_handler(message, get_photo_process_activity, fullname, phone_number)


@bot.message_handler(content_types=["photo", "document"])
def get_photo_process_activity(message: types.Message, fullname, phone_number):
    chat_id = message.chat.id

    file_id = __get_file_id(message)

    bot.send_message(chat_id, """
Выберите вид дейтельности из представленных ниже.

Если в данном списке нету деятельности, которую вы оказываете, можете написать ее.
""", reply_markup=services_menu())
    bot.register_next_step_handler(message, get_activity_process_registration, fullname, phone_number, file_id)


def get_activity_process_registration(message: types.Message, fullname, phone_number, file_id):
    chat_id = message.chat.id

    lastname, first_name, surname = fullname.split(" ")

    file = bot.get_file(file_id)
    filename = file.file_path.split("/")[-1]
    service_id = api.get_service_id(message.text)

    file_url = config.telegram_url.format(
        bot_token=config.BOT_TOKEN,
        file_path=file.file_path
    )

    photo = requests.get(file_url).content

    with open(filename, "wb") as file:
        file.write(photo)

    time.sleep(2)

    data_dict = {
        "first_name": first_name,
        "last_name": lastname,
        "surname": surname,
        "kind_of_activity": message.text,
        "telegram_chat_id": message.chat.id,
        "service": service_id['service_id'],
    }

    with open(filename, "rb") as file_io:
        api.create_service_profile(data_dict, {"document_photo": file_io})

    bot.send_photo(chat_id, photo=file_id, caption=f"""
ФИО: <b>{fullname}</b>
Номер телефона: <b>{phone_number}</b>
Вид деятельности: <b>{message.text}</b>
""", parse_mode="HTML")

    time.sleep(1)
    os.remove(filename)
