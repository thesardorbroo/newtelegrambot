from curses import keyname
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

languages = ReplyKeyboardMarkup(resize_keyboard=True,row_width=2).add(
    KeyboardButton("๐บ๐ฟuz"),KeyboardButton("๐ท๐บru"),
)

gender_btn = ReplyKeyboardMarkup(resize_keyboard=True,row_width=2).add(
    KeyboardButton("๐๐ปโโ๏ธ"),KeyboardButton("๐๐ปโโ๏ธ")
)

basic_buttons_ru = ReplyKeyboardMarkup(resize_keyboard=True,row_width=2,one_time_keyboard=True).add(
    KeyboardButton("๐ ะะฐัะฐัั ะดะธะฐะปะพะณ"),KeyboardButton("๐ ะะพะธัะบ")
)
basic_buttons = ReplyKeyboardMarkup(resize_keyboard=True,row_width=2,one_time_keyboard=True).add(
    KeyboardButton("๐ Sherik qidirish"),KeyboardButton("๐ qidirish")
)

main_keys = {
    "๐บ๐ฟuz":{
        "Base buttons": basic_buttons,
    },
    "๐ท๐บru":{
        "Base buttons": basic_buttons_ru,
    }
}