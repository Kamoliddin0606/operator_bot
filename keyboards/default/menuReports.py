from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menuReports = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='⬅️ previous'),
            KeyboardButton(text='❌ Cancel report'),
            
           
            

        ]
    ],
    resize_keyboard=True
)