from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from filters import IsPrivate
from loader import dp
from keyboards.default.menuKeyboard import menu


@dp.message_handler(IsPrivate(),CommandStart())
async def bot_start(message: types.Message):
     await message.answer(f"Привет, {message.from_user.full_name}!", reply_markup=menu)
