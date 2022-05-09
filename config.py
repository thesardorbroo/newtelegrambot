from aiogram import Bot,Dispatcher

from botdb import AnonDB

TOKEN = '5297025716:AAHWLEmC1zSHc2XGRI9hohW_fqPHcWzD7jw'
bot = Bot(TOKEN)
dp = Dispatcher(bot)
db = AnonDB()
