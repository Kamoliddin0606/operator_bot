from aiogram import types
from filters import IsPrivate
from loader import dp,bot
from aiogram.dispatcher.filters import Command
from data.config import ADMINS
from aiogram.dispatcher import FSMContext
 
from aiogram.dispatcher.filters.state import State
from states.contactWithAdminState import contactAdmin
from keyboards.default.returnMenu import menuReturn
from keyboards.default.menuKeyboard import menu
from keyboards.default.menuKeyboardAdmin import menuAdmin
from data.config import ADMINS
# Echo bot
@dp.message_handler( text ="👨🏽‍💻 Связаться с администратором")
async def getMyID(message: types.Message):
    await message.reply("""
‼️Принимаются только следующие заявки:
                        
🖋 Жалобы, связанные с ошибками отчетности
🖋 Обращения, связанные с подключением телеграм-аккаунта торгового представителя к системе К.И.Т.

📬Оставьте свое сообщение и я постараюсь ответить в ближайшее время:
                        """, reply_markup=menuReturn)
    await contactAdmin.messageToAdmin.set()

@dp.message_handler(state = contactAdmin.messageToAdmin)
async def cencelReport(message: types.Message, state:FSMContext):

    messageToAdmin = f'<b>message from:</b> {message.from_user.id} @{message.from_user.username}   {message.from_user.full_name}:\n\n <b>Message:</b> {message.text}'
    if str(message.from_user.id) not in ADMINS:
            await message.reply("Ваше сообщение было доставлено администратору", reply_markup=menu)
    else:
            await message.reply("Ваше сообщение было доставлено администратору", reply_markup=menuAdmin)
    
    
    await bot.send_message(ADMINS[0],messageToAdmin)
    await state.finish()

@dp.message_handler(state = contactAdmin.messageToAdmin, content_types=types.ContentTypes.PHOTO)
async def cencelReport(message: types.Message, state:FSMContext):

    messageToAdmin = f'<b>message from:</b> {message.from_user.id} @{message.from_user.username}   {message.from_user.full_name}:\n\n <b>Message:</b> {message.text}'
    if str(message.from_user.id) not in ADMINS:
            await message.reply("Ваше сообщение было доставлено администратору", reply_markup=menu)
    else:
            await message.reply("Ваше сообщение было доставлено администратору", reply_markup=menuAdmin)
    
    photos = message.photo

    
    photo = photos[0]

   
    file_id = photo.file_id
    await bot.send_photo(ADMINS[0], file_id,messageToAdmin)

    await state.finish()
