from aiogram.types import Message as msg

from config import dp,bot,db
from texts import *
from keys_ import *
from user_ import User

async def pressed_start(message: msg):
    print(message)
    fullname = ""
    if await db.is_user_exist(message.from_user.id):
        await db.update_user(message.from_user.id)
    else:
        if message.from_user.first_name == True and message.from_user.last_name == True:
            fullname = f"{message.from_user.first_name} {message.from_user.last_name}"
        else:
            fullname = message.from_user.username
        await db.adding_into(fullname,message.from_user.id)
        await bot.send_message(message.from_user.id,main_texts["Choose language"],reply_markup=languages)
        

async def message_is_text(message: msg, user: User):
    user_id = message.from_user.id
    text = message.text
    if user.step == 1:
        if text == "🇺🇿uz" or text == "🇷🇺ru":
            user.language = text
            await db.update_col_val(user_id,'language',text)
            await db.update_col_val(user_id,'step',2)
            await bot.send_message(user_id,main_texts[user.language]["Enter your age"])

        else:
            await message.answer(main_texts["Wrong choice"])

    elif user.step == 2 and text.isdigit():
        await db.update_col_val(user_id,'age',text)
        await db.update_col_val(user_id,'step',3)
        await bot.send_message(user_id,main_texts[user.language]["Your gender"],reply_markup=gender_btn)

    elif user.step == 3:
        if text == "🙍🏻‍♀️" or text == "🙎🏻‍♂️":
            await db.update_col_val(user_id,'gender',text)
            await db.update_col_val(user_id,'step',4)
            await bot.send_message(user_id,main_texts[user.language]["Please choose"],reply_markup=main_keys[user.language]["Base buttons"])
        else:
            await message.answer(main_texts["Wrong choice"])

async def main_function(message: msg, user: User):
    user_id = message.from_user.id
    text = message.text
    # if user.step == 4:
    #     await bot.send_message(user_id,main_texts[user.language]["Please choose"], reply_markup=main_keys[user.language]["Base buttons"])
    #     await db.update_col_val(user_id,'step',5)
    if user.step == 4:
        if text == "🚀 Sherik qidirish" or text == "🚀 Начать диалог":
            if await db.find_couple(user_id) == True:
                await bot.send_message(user_id,"User qidirilmoqda . . .")
                if await db.is_user_selected(user_id):
                    await db.update_col_val(user_id,'step',5)
                
                await main_function(message, user)
                
            else:
                await bot.send_message(user_id,"Keyinroq urinib ko'ring)")
        
    elif user.step == 5:
        pass
        # print(await bot.copy_message(user.couple_id,user.user_id,message.message_id))