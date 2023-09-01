from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menuAdmin = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='📊 Отправить отчет'),
            KeyboardButton(text='Мой 🆔'),
          

            
        ],
        [
            KeyboardButton(text='🆔 Группы и темы'),
            KeyboardButton(text='🆔 Участники группы'),

        ],
         [
            KeyboardButton(text='👨🏽‍💻 Связаться с администратором'),

        ]
        
    ],
    resize_keyboard=True
)