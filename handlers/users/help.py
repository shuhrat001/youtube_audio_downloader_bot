from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    
    await message.answer("Bu bot Youtube platformasidagi videolarni audio shaklini olishga yordam beradi. \nBotni ishga tushirish uchun /start tugmachasini bosing!")
