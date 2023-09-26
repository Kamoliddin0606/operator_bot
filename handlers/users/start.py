from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from filters import IsPrivate
from loader import dp
from keyboards.default.menuKeyboard import menu
from data.config import ADMINS
from keyboards.default.menuKeyboardAdmin import menuAdmin

@dp.message_handler(IsPrivate(),CommandStart())
async def bot_start(message: types.Message):
 #   await message.answer(f"Привет, {message.from_user.full_name}!", reply_markup=menu)

    if str(message.from_user.id) not in ADMINS:
        await message.answer(f"Привет, {message.from_user.full_name}!",reply_markup=menu)
    else:
        await message.answer(f"Привет, {message.from_user.full_name}!",reply_markup=menuAdmin) 
