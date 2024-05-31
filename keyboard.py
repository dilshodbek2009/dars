from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup


def nastroyka():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="Изменить язык🇷🇺"), KeyboardButton(text="Изменить номер телефона 📱"))
    rkm.row(KeyboardButton(text="Изменить имя✏️"), KeyboardButton(text="Назад ⬅️"))
    return rkm


def menu():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="Заказать 🛍"), KeyboardButton(text="Информация ℹ️"))
    rkm.row(KeyboardButton(text="Настройки⚙️"), KeyboardButton(text="Отзыв/комментарий  📩"))
    return rkm


def kontakt():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="Поделитесь своим контактом📞", request_contact=True))
    rkm.row(KeyboardButton(text="Назад ⬅"))
    return rkm


def otmen():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="Отменить ❌"))
    return rkm


def otmen1():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="Отменит"))
    return rkm

def next_menu():
    ikm = InlineKeyboardMarkup()
    ikm.row(InlineKeyboardButton(text="Русский 🇷🇺", callback_data="Русский 🇷🇺"))
    ikm.row(InlineKeyboardButton(text="English 🇺🇸", callback_data="English 🇺🇸"))
    ikm.row(InlineKeyboardButton(text="Õzbek🇺🇿", callback_data="Õzbek🇺🇿"))
    return ikm


def instagram():
    ikm = InlineKeyboardMarkup()
    ikm.row(InlineKeyboardButton(text="nstagram🎉", callback_data="instagram🎉"))
    return ikm