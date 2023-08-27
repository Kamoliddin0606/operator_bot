from aiogram import types
from filters import IsPrivate
from loader import dp
from aiogram.dispatcher.filters import Command

# Echo bot
@dp.message_handler( text ="Мой 🆔")
async def getMyID(message: types.Message):
    await message.reply("<b>🆔 Ваш идентификационный номер:</b> "+ "<i>"+str(message.from_user.id)+"</i>")

@dp.message_handler( commands='myid')
async def getMyID(message: types.Message):
    await message.reply("<b>🆔 Ваш идентификационный номер:</b> "+ "<i>"+str(message.from_user.id)+"</i>")  