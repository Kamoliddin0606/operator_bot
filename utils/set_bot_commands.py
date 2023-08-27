from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Запустить бота"),
            # types.BotCommand("help", "Instructions for using the bot"),
            types.BotCommand("myid", "Получить идентификационный номер пользователя"),
            types.BotCommand("report", "Отправить ежедневный отчет"),
            

        ]
    )
