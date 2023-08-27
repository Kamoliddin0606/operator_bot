from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='📊 Отправить отчет'),
            KeyboardButton(text='Мой 🆔'),
            
        ],
        [
            KeyboardButton(text='👨🏽‍💻 Связаться с администратором'),

        ]
        
    ],
    resize_keyboard=True
)