from aiogram.types import Message as msg
from aiogram import executor

import core
from config import dp,bot,db

@dp.message_handler(commands=['start'])
async def pressed_start(message: msg):
    await core.pressed_start(message)


@dp.message_handler()
async def user_send(message: msg):
    user = await db.make_object(message.from_user.id)
    if user.step < 4:
        await core.message_is_text(message,user)
    elif user.step > 3:
        await core.main_function(message,user)

if __name__ == "__main__":
    executor.start_polling(dp,skip_updates=True)