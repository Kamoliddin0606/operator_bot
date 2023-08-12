from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Send a report'),
            KeyboardButton(text='My ID'),
            

        ]
    ],
    resize_keyboard=True
)