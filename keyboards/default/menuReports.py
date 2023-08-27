from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menuReports = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='⬅️ Предыдущий'),
            KeyboardButton(text='❌ Отменить отчет'),
            
           
            

        ]
    ],
    resize_keyboard=True
)