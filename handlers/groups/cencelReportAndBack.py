from loader import dp
from aiogram import types
from states.reportFromSalesRepresentativeStates import reportSR
from keyboards.default.menuKeyboard import menu
@dp.message_handler(text='❌ Cancel report', state = None)
async def cencelReport(message: types.Message):
    await message.answer("<b>Main menu</b>", reply_markup=menu)
   