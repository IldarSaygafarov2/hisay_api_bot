from telebot import types


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
        types.KeyboardButton(text="Отправить номер телефона")
    )
    return kb
