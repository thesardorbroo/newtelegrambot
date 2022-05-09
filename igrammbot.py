# import logging
# from re import search
# from aiohttp import request
# import wikipedia
# from helperkeys import Keyboards
 
# from aiogram import Bot, Dispatcher, executor, types
# wikipedia.set_lang('ru')
# API_TOKEN = '5297025716:AAHWLEmC1zSHc2XGRI9hohW_fqPHcWzD7jw'

# logging.basicConfig(level=logging.INFO)

# bot = Bot(token=API_TOKEN)
# dp = Dispatcher(bot)

# @dp.message_handler(commands=['start', 'help'])
# async def send_welcome(message: types.Message):
#     await message.reply(f"Assalomu alaykum {message.from_user.username}\nMen Wikipediadan maqola topib beruvchi bot man ☺️")
#     await message.animation(message.chat.id,"Press")
# @dp.message_handler()
# async def echo(message: types.Message):
#     try:
#         search_i = wikipedia.summary(message.text)
#         await message.answer(search_i)
#         await message.answer_photo(photo="https%3A%2F%2Fscreenfiction.org%2Fcontent%2Fimage%2F0%2F61%2F323%2F64c58441-full.webp&imgrefurl=https%3A%2F%2Fscreenfiction.org%2Fen%2Fcharacter%2Fkimiko-the-female%2Fgallery&tbnid=H3J_ah8-7LaSkM&vet=12ahUKEwjDxdSK3Mr2AhUWdRQKHTd4DxQQMyg5egQIARBJ..i&docid=Uvdw2EeWlfrxQM&w=1074&h=1500&q=the%20boys%20kimiko&ved=2ahUKEwjDxdSK3Mr2AhUWdRQKHTd4DxQQMyg5egQIARBJ")
#     except:
#         await message.answer("Bunday maqola topilmadi 😔")

# if __name__ == '__main__':
#     executor.start_polling(dp, skip_updates=True)
# #%%
# import requests
# from pprint import pprint as print

# # https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@{apiVersion}/{endpoint}

# word = input("Enter word: ")

# url_word = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
# response = requests.get(url_word)
# jsondata = response.json()
# print(jsondata)

