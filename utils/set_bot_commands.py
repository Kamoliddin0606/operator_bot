from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Launch the bot"),
            # types.BotCommand("help", "Instructions for using the bot"),
            types.BotCommand("myid", "Get a user ID number"),

        ]
    )
