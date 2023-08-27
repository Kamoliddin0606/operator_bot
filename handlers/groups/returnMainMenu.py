from aiogram import types
from states.contactWithAdminState import contactAdmin

from loader import dp
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State
from keyboards.default.menuKeyboard import menu
from keyboards.default.menuKeyboardAdmin import menuAdmin
from data.config import ADMINS

@dp.message_handler(state=contactAdmin.messageToAdmin, text ="⏪ Вернуться в главное меню")
async def getMyID(message: types.Message, state:FSMContext):
    if str(message.from_user.id) in ADMINS:
        await message.answer("Menu", reply_markup=menuAdmin)
    else:
        await message.answer("Menu", reply_markup=menu)
    await state.finish()

@dp.message_handler( text ="⏪ Вернуться в главное меню")
async def getMyID(message: types.Message):
    if str(message.from_user.id) in ADMINS:
        await message.answer("Menu", reply_markup=menuAdmin)
    else:
        await message.answer("Menu", reply_markup=menu)
    
    