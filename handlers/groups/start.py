from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from filters import IsGroup
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.default.menuKeyboard import menu
from keyboards.default.menuKeyboardAdmin import menuAdmin
from data.config import ADMINS
from loader import dp, bot


@dp.message_handler(IsGroup(),CommandStart())
async def bot_start(message: types.Message):

        if str(message.from_user.id) not in ADMINS:
            await message.answer("Бот запущен! ",reply_markup=menu)
        else:
            await message.answer("Бот запущен! ",reply_markup=menuAdmin)   

    