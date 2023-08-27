from aiogram import types
from states.contactWithAdminState import contactAdmin

from loader import dp
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State
from keyboards.default.menuKeyboard import menu

@dp.message_handler(state=contactAdmin.messageToAdmin, text ="⏪ Вернуться в главное меню")
async def getMyID(message: types.Message, state:FSMContext):
    await message.answer("Menu", reply_markup=menu)
    await state.finish()

@dp.message_handler( text ="⏪ Вернуться в главное меню")
async def getMyID(message: types.Message):
    await message.reply("Menu", reply_markup=menu)
    