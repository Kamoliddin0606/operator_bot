from aiogram import types
from filters import IsPrivate
from loader import dp, bot
from filters import AdminFilter

@dp.message_handler(AdminFilter(),text=['🆔 Участники группы'])
async def get_members( message: types.Message):
    # Get a list of all the chats your bot is in
    chats = await bot.get_chat_members_count(chat_id=message.chat.id)
    
    for chat in chats:
        chat_id = chat.chat.id
        chat_type = chat.chat.type
        
        # Only process group and supergroup chats
        if chat_type in ('group', 'supergroup'):
            members = await bot.get_chat_members_count(chat_id=chat_id)
            
            await message.reply(f"Chat ID: {chat_id}, Members: {members}")
