from curses import keyname
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

languages = ReplyKeyboardMarkup(resize_keyboard=True,row_width=2).add(
    KeyboardButton("🇺🇿uz"),KeyboardButton("🇷🇺ru"),
)

gender_btn = ReplyKeyboardMarkup(resize_keyboard=True,row_width=2).add(
    KeyboardButton("🙍🏻‍♀️"),KeyboardButton("🙎🏻‍♂️")
)

basic_buttons_ru = ReplyKeyboardMarkup(resize_keyboard=True,row_width=2,one_time_keyboard=True).add(
    KeyboardButton("🚀 Начать диалог"),KeyboardButton("🔎 Поиск")
)
basic_buttons = ReplyKeyboardMarkup(resize_keyboard=True,row_width=2,one_time_keyboard=True).add(
    KeyboardButton("🚀 Sherik qidirish"),KeyboardButton("🔎 qidirish")
)

main_keys = {
    "🇺🇿uz":{
        "Base buttons": basic_buttons,
    },
    "🇷🇺ru":{
        "Base buttons": basic_buttons_ru,
    }
}