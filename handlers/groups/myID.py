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
@dp.message_handler( text="🆔 группы и темы")
async def getMyID(message: types.Message):
     if message.chat.type == 'group' or message.chat.type == 'supergroup':
        topic_id = message.message_thread_id
       # await message.reply(f"The topic ID is: {topic_id}")
        await message.reply("<i>🆔 номер группы: "+str(message.chat.id)+"\n🆔 номер темы: " +str(topic_id)+"</i>") 