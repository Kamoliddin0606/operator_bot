from aiogram import types
from filters import IsPrivate
from loader import dp,bot
from aiogram.dispatcher.filters import Command
from data.config import ADMINS
from aiogram.dispatcher import FSMContext
 
from aiogram.dispatcher.filters.state import State
from states.contactWithAdminState import contactAdmin

# Echo bot
@dp.message_handler( text ="👨🏽‍💻 Contact with admin")
async def getMyID(message: types.Message):
    await message.reply("""
‼️Принимаются только следующие заявки:
                        
🖋 Жалобы, связанные с ошибками отчетности
🖋 Обращения, связанные с подключением телеграм-аккаунта торгового представителя к системе К.И.Т.

📬Оставьте свое сообщение и я постараюсь ответить в ближайшее время:
                        """)
    await contactAdmin.messageToAdmin.set()

@dp.message_handler(state = contactAdmin.messageToAdmin)
async def cencelReport(message: types.Message, state:FSMContext):

    messageToAdmin = f'<b>message from:</b> {message.from_user.id} @{message.from_user.username}   {message.from_user.full_name}:\n\n <b>Message:</b> {message.text}'
    for admin in ADMINS:

        await bot.send_message(admin,messageToAdmin)
    await state.finish()

