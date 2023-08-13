from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='📊 Send a report'),
            KeyboardButton(text='My 🆔'),
            
        ],
        [
            KeyboardButton(text='👨🏽‍💻 Contact with admin'),

        ]
        
    ],
    resize_keyboard=True
)