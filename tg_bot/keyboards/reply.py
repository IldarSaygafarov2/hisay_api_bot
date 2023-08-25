from telebot import types
from tg_bot.helpers import api


def start_menu():
    kb = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)

    kb.add(*[
        types.KeyboardButton(text="Пользователь"),
        types.KeyboardButton(text="Сервис"),
    ])
    return kb


def phone_number_button():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(
        types.KeyboardButton(text="Отправить номер телефона", request_contact=True)
    )
    return kb


def services_menu():
    kb = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    services = api.get_services()
    buttons = [
        types.KeyboardButton(text=service['name'])
        for service in services
    ]
    kb.add(*buttons)
    return kb
