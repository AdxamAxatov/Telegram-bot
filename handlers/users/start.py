from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import InputFile
from keyboards.inline.inlineKeyboards import menu_start

from loader import dp

@dp.message_handler(CommandStart())
async def bot_start(msg: types.Message):
    photo_file = InputFile(path_or_bytesio="photos\photo_2024-10-17_15-37-03.jpg")
    description = f"Hello {msg.from_user.full_name}\n<b>My name is Otajon Bozorboyev</b>"
    await msg.answer_photo(photo_file, caption=description, reply_markup=menu_start )
